#!/usr/bin/python3

import cgi
import subprocess
import cgitb 

print("context-type: text/html")
print()

form = cgi.FieldStorage()
print()

#webserver Configuration
subprocess.getoutput("yum install httpd -y")
subprocess.getoutput("systemctl stop firewalld")
subprocess.getoutput("systemctl enable httpd --now")

#Webpage Creation
page_name = form.getvalue('page_name')
content = form.getvalue('content')
output1 = subprocess.getoutput("sudo touch /var/www/html/{}.html".format(page_name))
output2 = subprocess.getoutput(f"echo \'{content}\' | sudo tee /var/www/html/\'{page_name}\'.html > /dev/null ")
ip = subprocess.getoutput("hostname -I | awk '{print $1}'")
print("""


       Enter this IP to get the web page

       ----------------------------
       http://{0}/{1}.html 
       _____________________________

""".format(ip,page_name))
