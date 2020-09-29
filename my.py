#!/usr/bin/python3
import cgi
print("content-type : text/html")
print()


form=cgi.fieldstorage()
cmd=form.getvalue()

import subprocess as sp

z=sp.getoutputvalue(cmd)
print(z)
print("hello")
