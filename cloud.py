#!/usr/bin/python
import cgi,cgitb
cgitb.enable()

print "Content-type:text/html"
print ""
form=cgi.FieldStorage()
x=form.getvalue("user")
y=form.getvalue("pass")
z=form.getvalue("email")
v=form.getvalue("contact")


f=open('user.txt','w')
f.write(x)
f.close()

f=open('pass.txt','w')
f.write(y)
f.close()

f=open('email.txt','w')
f.write(z)
f.close()

f=open('cont.txt','w')
f.write(v)
f.close()

f=open('user.txt','r')
s=f.read()
f.close()

f=open('pass.txt','r')
t=f.read()
f.close()

if  s == "root"  and   t == "redhat" :
		print "<META HTTP-EQUIV=\"refresh\"content=\"5;url=http://192.168.122.1/services.html\">\n"

else :
    	        print "<META HTTP-EQUIV=\"refresh\"content=\"5;url=http://192.168.122.1/index.html\">\n"





