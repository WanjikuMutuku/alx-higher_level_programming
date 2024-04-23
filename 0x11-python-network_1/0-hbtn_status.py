#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    body = response.read()
    content_type = response.info().get_content_type()
    utf8_content = body.decode('utf-8')

print("Body response:")
print(f"    - type: {type(body)}")
print(f"    - content: {body}")
print(f"    - utf8 content: {utf8_content}")
