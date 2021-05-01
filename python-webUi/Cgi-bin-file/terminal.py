#!/usr/bin/python3

import cgi
import subprocess 

print("context-type: text/html")
print()

mydata = cgi.FieldStorage()
myx = mydata.getvalue("l_cmd");
output = subprocess.getoutput(myx)

print("""
            --------------------------------
               LINUX CMD OUTPUT CONSOLE
            --------------------------------
            
{0}           
""".format(output))





