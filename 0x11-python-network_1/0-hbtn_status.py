#!/usr/bin/python3
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read()
    utf8_content = body.decode('utf-8')

print("Body response:")
print("    - type: {}".format(type(body)))
print("    - content: {}".format(body))
print("    - utf8 content: {}".format(utf8_content))
