#!/usr/bin/python
import cgi ,cgitb ,commands
cgitb.enable()
print "Content-type:text/html"
print ""
form=cgi.FieldStorage()
x=form.getvalue("storage")
#y=form.getvalue("value")

'''
f=open('ss.txt','w')
f.write(x)
f.close()

f=open('st.txt','w')
f.write(y)
f.close()

f=open('ss.txt','r')
f.read()
f.close()

f=open('st.txt','w')
f.write(y)
f.close()
'''

if x == "Object-type" :
         print "<META HTTP-EQUIV=\"refresh\"content=\"5;url=http://192.168.122.1/staas1.html\">\n"

else :
        print "<META HTTP-EQUIV=\"refresh\"content=\"5;url=http://192.168.122.1/services.html\">\n"

 
