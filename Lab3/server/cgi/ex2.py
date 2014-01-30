#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()

name = form.getvalue('name')

family = form.getvalue('family')

print "Content-type: text/html"
print
print "<html><head><title>Page 2</title></head>"
print "<body>"
if(name == None):
	print "<p>No name given.</p>"
else:
	print "<p>Name: ", name, "</p>"
if(family == None):
	print "<p>No family given.</p>"
else:
	print "<p>Family: ", family, "</p>"

print "<form method=\"post\" action=\"/cgi/ex1.py\">"
print "<label for=\"name\">Name: </label>"
print "<input id=\"name\" type=\"text\" name=\"name\" />"
print "<br />"
print "<label for=\"family\">Family: </label>"
print "<input id=\"family\" type=\"text\" name=\"family\" />"
print "<br />"
print "<label for=\"age\">Age: </label>"
print "<input id=\"age\" type=\"text\" name=\"age\" />"
print "<br />"
print "<label for=\"mainhobby\">Main Hobby: </label>"
print "<input id=\"mainhobby\" type=\"text\" name=\"mainhobby\" />"
print "<br />"
print "<input type=\"submit\" value=\"Submit\" />"
print "</form>"
print "</body></html>"