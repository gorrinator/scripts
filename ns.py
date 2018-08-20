#Script will return results from command line arguments (DNS Record Type & Domain), e.g python ns.py a google.com
import requests
import sys
record = str(sys.argv[1]) # commandline input for the specific record type (A|AAAA|CNAME|MX|NS|PTR|SOA|TXT).
domain = str(sys.argv[2]) # command line input for the domain name you would like to grab the records for.
response = requests.get("https://dns-api.org//%s//%s" %(record,domain)) # Querys an API to run a lookup on the domain for the specific record type.
status = (response.status_code)
if status == int(200):
 print(response.content) #if the API provides a HTTP status of ok the script will print all of the relevant DNS results for the specificed domain namme.
else:
 print('An error %s occured, API may be down'%(status)) # advises the user if there may be an issue with the API if a HTTP response code other than OK  is recieved.
