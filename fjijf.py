"""
Finds Fabric mods with an embedded JAR dependency
"""
import json
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile, is_zipfile

d = input("dir > ")

jars = {}


def recurse(f, n, o, t):
    if is_zipfile(f):
        with ZipFile(f) as zf:
            with zf.open("fabric.mod.json") as j:
                j.seek(0)
                prop = json.load(j, strict=False)

            l = {}

            if "jars" in prop:
                for j in prop["jars"]:
                    l[j["file"].split("/")[-1]] = recurse(
                        BytesIO(zf.read(j["file"])), j["file"].split("/")[-1],
                        o, False,
                    )

            if l:
                print(f"'{n}' embeds; {', '.join(l)}")

                if t:
                    o[n] = l

                return l
    return None


for p in Path(d).rglob("*.jar"):
    # print(p)
    recurse(str(p), p.name, jars, True)

if jars:
    with open(Path(d) / "output.json", "w+") as f:
        f.write(json.dumps(jars, indent=4, sort_keys=True))
