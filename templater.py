#! /usr/bin/env python

import os
import sys
import copy
import subprocess

DEFAULT_TITLE = "Rachel E. McCoy"

# Warning for the top of output files
WARNING = '''



 <!--
 WARNING!!!
 This is an autogenerated file. All changes will be overwritten on
 next templating. You probably want to edit the "-template.html" file.
 -->




'''

def template(root):

    with open("components/head.html") as f:
        head = [WARNING, "<!DOCTYPE html>", "<head>"] + f.readlines()

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
                outpath = os.path.join(dirname, file.replace("-template", ""))
                css_file = file.replace("-template.html", ".css")
            elif file.find(".py") >= 1 and file != "templater.py":
                contents = [subprocess.check_output(os.path.join(dirname,file))]
                outpath = os.path.join(dirname, file.replace(".py", ".html"))
                css_file = file.replace(".py", ".css")
            else:
                continue

            page_head = copy.copy(head)
            title_path = outpath.replace(".html", "-title.html")
            if os.path.exists(title_path):
                with open(title_path) as f:
                    title = f.readline()    
            else:
                title = DEFAULT_TITLE

            page_head.append("<title>" + title + "</title>")


            css_path = os.path.join(dirname, css_file)
            if(os.path.exists(css_path)):
                page_head.append("<link rel=\"stylesheet\" href=\"" + css_file + "\">")

            page_head.append("</head>")


            data = page_head + header + contents + footer

            with open(outpath, "w") as f:
                f.writelines(data)

            print(outpath)


if __name__ == "__main__":
    template(".")