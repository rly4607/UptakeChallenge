#!/usr/bin/python

import struct
import array
import base64
import webbrowser

print ""
print "This is a test at the Uptake Challenge Billboard..."

testString = "curiosity"

print ""

encodedString = base64.b64encode(testString)

print ""
print "testString: ", testString
print "encoded String: ", encodedString
print ""

url = "https://" + encodedString + ".uptake.com";

print url

webbrowser.open_new(url)
