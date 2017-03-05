#!/usr/bin/python

import cgi,cgitb,os,commands

cgitb.enable()

print "Content-type:text/html"
print ""

form=cgi.FieldStorage()
a=form.getvalue("name")
b=form.getvalue("size")

a=commands.getstatusoutput("sudo lvcreate -L "+b+" -n "+a+" /dev/myvg")
print a
'''
print "<pre>"
print h
print "</pre>"

print "<pre>"
print "os.system(' lvcreate -L ' + str(b) + ' -n ' + str(a) + ' /dev/vg0')"
print "</pre>"
'''
