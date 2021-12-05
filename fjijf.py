"""
Finds JAR files with an embedded JAR dependency
"""

from pathlib import Path
from zipfile import ZipFile, is_zipfile

d = input("dir > ")

for p in Path(d).rglob("*.jar"):
    # print(p)

    if is_zipfile(str(p)):
        with ZipFile(str(p)) as zf:
            # print(zf)

            l = []

            for n in zf.namelist():
                if "jars" in n:
                    l.append(n.split("/")[-1])

            if l:
                print(f"'{p.name}' embeds; {', '.join(l)}")
