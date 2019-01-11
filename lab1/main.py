#!/usr/bin/env python

# Lab 1 - CMPUT 401

import requests

# print(requests.__version__)
request = requests.get("https://raw.githubusercontent.com/olivaC/cmput404Labs/master/lab1/main.py")

# print(request)
# print(dir(request))
# print(request.status_code)
print(request.text)

