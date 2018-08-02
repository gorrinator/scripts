#!/usr/bin/env python
import requests
import sys
record = str(sys.argv[1])
domain = str(sys.argv[2])
response = requests.get("https://dns-api.org//%s//%s" %(record,domain))
status = (response.status_code)
if status == int(200):
 print(response.content)
else:
 print('An error %s occured, API may be down'%(status))
