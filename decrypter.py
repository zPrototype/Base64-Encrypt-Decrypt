#!/usr/bin/python3
import os
import base64

home = os.path.expanduser("~")

for root, dirs, files in os.walk(home):
    files = list(filter(lambda f: f.endswith(".encrypted"), files))
    for file in files:
        path = os.path.join(root, file)
        with open(path, "rb") as f:
            dec = base64.b64decode(f.read())
        with open(path, "wb") as f:
            f.write(dec)
        os.rename(path, path.replace(".encrypted", ""))
