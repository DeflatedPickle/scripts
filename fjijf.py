"""
Finds Fabric mods with an embedded JAR dependency
"""
import json
from pathlib import Path
from zipfile import ZipFile, is_zipfile

d = input("dir > ")

jars = {}

for p in Path(d).rglob("*.jar"):
    # print(p)

    if is_zipfile(str(p)):
        with ZipFile(str(p)) as zf:
            # print(zf)

            with zf.open("fabric.mod.json") as j:
                j.seek(0)
                prop = json.load(j, strict=False)

            l = []

            if "jars" in prop:
                for j in prop["jars"]:
                    l.append(j["file"].split("/")[-1])

            if l:
                print(f"'{p.name}' embeds; {', '.join(l)}")
                jars[p.name] = l

if jars:
    with open(Path(d) / "output.json", "w+") as f:
        f.write(json.dumps(jars, indent=4, sort_keys=True))
