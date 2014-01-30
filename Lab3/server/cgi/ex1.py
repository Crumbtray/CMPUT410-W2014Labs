#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()

name = form.getvalue('name')

family = form.getvalue('family')

age = form.getvalue('age')

hobby = form.getvalue('mainhobby')

print "Content-type: text/html"
print
print "<html><head><title>Page 1</title></head>"
print "<body>"
if(name == None):
	print "<p>No name given.</p>"
else:
	print "<p>Name: ", name, "</p>"
if(family == None):
	print "<p>No family given.</p>"
else:
	print "<p>Family: ", family, "</p>"
if(age == None):
	print "<p>No age given.</p>"
else:
	print "<p>Age: ", age, "</p>"
if(hobby == None):
	print "<p>No main hobby given.</p>"
else:
	print "<p>Main Hobby: ", hobby, "</p>"

print "<form method=\"post\" action=\"/cgi/ex2.py\">"
print "<label for=\"name\">Name: </label>"
print "<input id=\"name\" type=\"text\" name=\"name\" />"
print "<br />"
print "<label for=\"family\">Family: </label>"
print "<input id=\"family\" type=\"text\" name=\"family\" />"
print "<br />"
print "<input type=\"submit\" value=\"Submit\" />"
print "</form>"
print "</body></html>"