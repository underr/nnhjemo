#!/usr/bin/env python3
import homeru
from mako.template import Template
from os.path import expanduser

home = expanduser("~")
links = homeru.parse(home + '/.links.ho')

mytemplate = Template(filename='./tmpl.html')

print("Writting to file...\n...")
with open("dist/index.html", "wb") as F:
    F.write(bytes(mytemplate.render(links=links), 'UTF-8'))
print("Done.")
