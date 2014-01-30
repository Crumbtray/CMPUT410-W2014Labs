#!/usr/bin/env python

print "Content-type: text/html"
print
print "<html><head><title>Test URL Encoding</title></head><body>"
print "<a href=\"http://localhost:8000/cgi/test_urlencode.py?first=Jack&last=Trades\">Link </a>"
print "</body></html>"