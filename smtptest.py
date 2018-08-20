#!/usr/bin/env python
import requests
import sys
email = str(sys.argv[1]) # grabs the email address from the command line
apikey = '20fc138403318af273d4f828088899c4' #API Key

response = requests.get("https://apilayer.net/api/check?access_key=%s&email=%s" %(apikey,email)) #  queries the mailboxlayer API to see if the email address is valid and exists.
print(response.text) # prints the response from the API in JSON.
