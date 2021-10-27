import subprocess
import os

def getDirListing(path):
    listing = {"folders":[],"files":[]}
    result = subprocess.Popen(['git', 'ls-files'], cwd=path, stdout=subprocess.PIPE)
    out, _ = result.communicate()
    for f in out.decode('utf-8').split('\n'):
        if "/" in f:
            if f.split("/")[0] not in listing["folders"]:
                listing['folders'].append(f.split("/")[0])
        else:
            if f not in listing["files"] and f != "":
                listing['files'].append(f)
    listing['folders'].sort()
    listing['files'].sort()
    return listing