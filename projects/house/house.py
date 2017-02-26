#! /usr/bin/env python

import os
import sys

import jinja2 

IMAGE_DIR = "imgs"

def render(template_loc, file_name, **context):

    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_loc+'/')
    ).get_template(file_name).render(context)


scriptpath = os.path.realpath(__file__)
splt = os.path.split(scriptpath)
directory = splt[0]
file = splt[1]

os.chdir(directory)
images = os.listdir(os.path.join(directory, IMAGE_DIR))
images = [os.path.join(IMAGE_DIR, x) for x in images]

templatefile = file.replace(".py", "-template.j2")

rendered = render(directory, templatefile, images=images)

sys.stdout.write(rendered)


