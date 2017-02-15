#! /usr/bin/env python

import os
import sys

def template(root):
    with open("components/header.html") as f:
        header = f.readlines()

    with open("components/footer.html") as f:
        footer = f.readlines()


    for dirname, subdirlist, filelist in os.walk(root):
        for file in filelist:
            if file.find("-template.html") > 0:

                inpath = os.path.join(dirname,file)
                with open(inpath) as f:
                    contents = f.readlines()

                data = header + contents + footer

                outpath = os.path.join(dirname, file.replace("-template", ""))
                with open(outpath, "w") as f:
                    f.writelines(data)



if __name__ == "__main__":
    template(".")