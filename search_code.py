import os
import sys

dir = sys.argv[1]
key = sys.argv[2]

def search(dir, key):
    for (path, subdirs, files) in os.walk(dir):
        for file in files:
            if file[-3:] != ".py":
                continue
            file_path = dir+"/"+file
            if not os.path.exists(file_path):
                continue
            fopen = open(file_path, "r")
            for i, line in enumerate(fopen):
                if key in line:
                    print(file_path, ":", i)
            fopen.close()
        if len(subdirs):
            for subdir in subdirs:
                search(dir+"/"+subdir, key)

search(dir, key)
