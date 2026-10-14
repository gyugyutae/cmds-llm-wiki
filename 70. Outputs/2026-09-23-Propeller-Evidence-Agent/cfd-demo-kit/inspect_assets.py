"""Static asset checks only: no CFD execution or physical validation."""
from pathlib import Path
import json
import struct
import xml.etree.ElementTree as ET
import h5py
import trimesh

ROOT = Path(__file__).resolve().parent

def main():
    result = {"solverExecuted": False, "hdf5": [], "geometry": []}
    for path in (ROOT / "assets").rglob("*.h5"):
        item = {"path": str(path.relative_to(ROOT)), "datasets": [], "attributes": {}}
        with h5py.File(path) as handle:
            item["attributes"] = {key: str(value) for key, value in handle.attrs.items()}
            def visit(name, obj):
                if isinstance(obj, h5py.Dataset):
                    record = {"name": name, "shape": list(obj.shape), "dtype": str(obj.dtype)}
                    if obj.size < 100:
                        value = str(obj[()])
                        record["value"] = value[:1500]
                        record["valueTruncated"] = len(value) > 1500
                    item["datasets"].append(record)
            handle.visititems(visit)
            topology = handle["meshes/1/cells/zoneTopology"]
            item["cellCount"] = int(sum(topology["maxId"][()] - topology["minId"][()] + 1))
            item["cellZones"] = str(topology["name"][()])
        result["hdf5"].append(item)
    for path in (ROOT / "assets" / "openfoam").rglob("prop.stl"):
        mesh = trimesh.load_mesh(path)
        result["geometry"].append({"path": str(path.relative_to(ROOT)),
            "faces": len(mesh.faces), "vertices": len(mesh.vertices),
            "watertight": bool(mesh.is_watertight), "boundsNativeUnits": mesh.bounds.tolist(),
            "unitsConfirmed": False})
    path = ROOT / "assets/nasa/X-57.vsp3"
    document = ET.parse(path)
    result["nasaVsp"] = {"xmlParsed": True, "rootTag": document.getroot().tag,
                         "propellerGeometryCount": sum(1 for node in document.iter("TypeName") if node.text == "Propeller")}
    path = ROOT / "assets/nasa/X-57.glb"
    with path.open("rb") as stream:
        magic, version, length = struct.unpack("<4sII", stream.read(12))
    result["nasaGlb"] = {"magic": magic.decode(), "version": version,
                         "declaredSizeMatches": length == path.stat().st_size}
    foam_root = next((ROOT / "assets/openfoam").glob("*-extracted/*"))
    result["openfoam"] = {"hasVolumeMesh": all((foam_root / "simulationTemplate/constant/polyMesh" / name).exists()
                           for name in ["points", "faces", "owner", "neighbour", "boundary"]),
                           "mrf": (foam_root / "simulationTemplate/constant/MRFProperties").read_text(),
                           "controlDict": (foam_root / "simulationTemplate/system/controlDict").read_text(),
                           "forces": (foam_root / "simulationTemplate/system/forces").read_text()}
    (ROOT / "inspection.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({"hdf5Files": len(result["hdf5"]), "geometry": result["geometry"],
                      "nasaVsp": result["nasaVsp"], "nasaGlb": result["nasaGlb"],
                      "hasOpenfoamVolumeMesh": result["openfoam"]["hasVolumeMesh"],
                      "solverExecuted": False}, indent=2))

if __name__ == "__main__":
    main()
