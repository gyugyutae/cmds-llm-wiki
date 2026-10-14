"""Real Fluent connection probe. Requires an already-running 2026 R1 session.

This is a connection/calculation smoke test, not a convergence or physics proof.
Loads the bundled axial-fan case into the connected session; use a fresh session.
"""
import argparse
import json
import math
from pathlib import Path
import sys
import time

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--server-info", required=True)
    parser.add_argument("--rpm", type=float)
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--iterations", type=int, default=20)
    args = parser.parse_args()
    if args.rpm is not None and (not math.isfinite(args.rpm) or args.rpm <= 0):
        parser.error("RPM must be finite and positive")
    if not 1 <= args.iterations <= 10000:
        parser.error("Iterations must be between 1 and 10000")
    root = Path(__file__).resolve().parent
    output = root / "runs" / time.strftime("%Y%m%d-%H%M%S")
    output.mkdir(parents=True, exist_ok=False)
    record = {"status": "started", "solverExecuted": False, "convergenceVerified": False,
              "caseRole": "ducted axial fan, not an aircraft propeller",
              "units": {"axialForce": "N", "torque": "N m"}}
    def save():
        (output / "probe.json").write_text(json.dumps(record, indent=2, default=str), encoding="utf-8")
    try:
        import ansys.fluent.core as pyfluent
        solver = pyfluent.connect_to_fluent(server_info_file_name=args.server_info)
        solver.settings.file.read_case(file_name=str(root / "assets/ansys-axial-fan/axial_fan.cas.h5"))
        solver.settings.mesh.check()
        settings = solver.settings
        frame = settings.setup.cell_zone_conditions.fluid["rotating-fan"].reference_frame
        record["before"] = frame.get_state()
        record["namedExpressionsBefore"] = settings.setup.named_expressions.get_state()
        if args.rpm is not None:
            planned = args.rpm * 2 * math.pi / 60
            frame.mrf_omega.value.set_state(planned)
            actual = float(frame.mrf_omega.value.get_state())
            record["rpmVerification"] = {"plannedRpm": args.rpm, "plannedRadS": planned,
                "actualRadS": actual, "matches": math.isclose(actual, planned, rel_tol=1e-9, abs_tol=1e-8)}
            if not record["rpmVerification"]["matches"]:
                raise RuntimeError("RPM readback mismatch; execution blocked")
        record["after"] = frame.get_state()
        record["existingReports"] = settings.solution.report_definitions.get_state()
        save()
        if args.run:
            if args.rpm is None:
                raise RuntimeError("For this probe --run requires an explicit --rpm")
            if not frame.frame_motion.get_state():
                raise RuntimeError("MRF is not active")
            axis = [float(frame.reference_frame_axis_direction[i].value.get_state()) for i in range(3)]
            if any(not math.isclose(a, b, abs_tol=1e-9) for a,b in zip(axis, [0,1,0])):
                raise RuntimeError("Bundled fan probe requires Y rotation axis")
            reports = settings.solution.report_definitions
            # Include fan blade and tip surfaces; this choice requires expert review.
            walls = ["fan-walls", "fan-tip-wall"]
            reports.force.create(name="probe-axial-force")
            reports.force["probe-axial-force"].set_state({"report_type": "force",
                "zones": walls, "force_vector": [0,1,0], "report_output_type": "Force"})
            reports.moment.create(name="probe-torque")
            reports.moment["probe-torque"].set_state({"report_type": "moment",
                "zones": walls, "mom_axis": [0,1,0], "mom_center": [0,0,0], "report_output_type": "Moment"})
            record["probeReportSettings"] = {"force": reports.force["probe-axial-force"].get_state(),
                "moment": reports.moment["probe-torque"].get_state()}
            settings.solution.initialization.hybrid_initialize()
            settings.solution.run_calculation.iterate(iter_count=args.iterations)
            record["solverExecuted"] = True
            record["results"] = reports.compute(report_defs=["probe-axial-force", "probe-torque"])
            settings.file.write_case_data(file_name=str(output / "probe.cas.h5"))
        record["status"] = "probe_completed_not_physics_validated"
    except Exception as error:
        record["status"] = "failed"
        record["error"] = repr(error)
        save()
        raise
    finally:
        save()
        print(output / "probe.json")

if __name__ == "__main__":
    main()
