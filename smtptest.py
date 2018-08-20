#!/usr/bin/env python
import requests
import sys
email = str(sys.argv[1])
apikey = '20fc138403318af273d4f828088899c4'

response = requests.get("https://apilayer.net/api/check?access_key=%s&email=%s" %(apikey,email))
print(response.text)

