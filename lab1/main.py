#!/usr/bin/env python

# Lab 1 - CMPUT 401

import requests

# print(requests.__version__)
request = requests.get("http://www.google.com")

print(dir(request))
print(request.status_code)
# print(request.text)