"""Download public reference assets; does not execute third-party code or solvers."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parent

def read_url(url):
    return subprocess.run(["curl", "-sSL", "--fail", "--retry", "2", "--max-time", "180", url],
                          check=True, capture_output=True).stdout

def fetch(item):
    name, url = item
    path = ROOT / "assets" / name
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        data = read_url(url)
        if data.startswith(b"version https://git-lfs.github.com/spec/"):
            raise ValueError("Git LFS pointer, not asset content")
        path.write_bytes(data)
        result = {"path": str(path.relative_to(ROOT)), "sourceUrl": url,
                  "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
                  "status": "downloaded", "solverVerified": False}
        if name.endswith((".zip", ".zipx")):
            with zipfile.ZipFile(path) as archive:
                result["archiveMembers"] = archive.namelist()
                target = path.parent / (path.stem + "-extracted")
                try:
                    for member in archive.infolist():
                        destination = (target / member.filename).resolve()
                        if not destination.is_relative_to(target.resolve()):
                            raise ValueError("Unsafe archive path")
                        if (member.external_attr >> 16) & 0o170000 == 0o120000:
                            raise ValueError("Archive symlink")
                    archive.extractall(target)
                    result["extractedPath"] = str(target.relative_to(ROOT))
                except (NotImplementedError, RuntimeError) as error:
                    result["extractionError"] = str(error)
        return result
    except Exception as error:
        return {"path": name, "sourceUrl": url, "status": "failed", "error": str(error)}

def main():
    items = [
        ("ansys-axial-fan/axial_fan.cas.h5", "https://media.githubusercontent.com/media/ansys/example-data/main/pyfluent/axial_fan_performance_curve/axial_fan.cas.h5"),
        ("ansys-axial-fan/axial_fan.msh.h5", "https://media.githubusercontent.com/media/ansys/example-data/main/pyfluent/axial_fan_performance_curve/axial_fan.msh.h5"),
        ("openfoam/propeller-OpenFOAM.zip", "https://codeload.github.com/skfelix/propeller-OpenFOAM/zip/eaa8e70e8ecc2c48ba9927cac5feb83c8e39e416"),
        ("fluent-candidate/HPC-example-ANSYS.zip", "https://codeload.github.com/rtuhpc/HPC-example-ANSYS/zip/5c9089976025d80b9b1fff7b1095f38f7c746e25"),
        ("nasa/X-57.glb", "https://raw.githubusercontent.com/nasa/NASA-3D-Resources/master/3D%20Models/X-57/X-57.glb"),
        ("nasa/X-57.vsp3", "https://raw.githubusercontent.com/nasa/NASA-3D-Resources/master/3D%20Models/X-57/X-57.vsp3"),
        ("apc/APC2BEM.jl", "https://raw.githubusercontent.com/jamesjhu/APC2BEM/main/apc2bem.jl"),
        ("apc/APC2BEM-LICENSE", "https://raw.githubusercontent.com/jamesjhu/APC2BEM/main/LICENSE"),
    ]
    page = read_url("https://www.apcprop.com/technical-information/file-downloads/").decode()
    for url in sorted(set(re.findall(r'https[^\s"<>]+\.zipx', page))):
        if "PE0" in url or "PERFILES" in url:
            items.append(("apc/" + url.rsplit("/", 1)[-1], url))
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(fetch, items))
    (ROOT / "manifest.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    for result in results:
        print(result["status"], result["path"], result.get("bytes", ""), result.get("error", ""), result.get("extractionError", ""))

if __name__ == "__main__":
    main()
