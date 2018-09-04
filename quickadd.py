#!/usr/bin/env python
from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
SCOPES = 'https://www.googleapis.com/auth/calendar'
import sys
time = str(sys.argv[1])
date = str(sys.argv[2])
input = time + date
def main():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))
    created_event = service.events().quickAdd(
    calendarId='neto.com.au_t6v4op72aj7d279hhbacq1h32o@group.calendar.google.com',
    text='%s %s Go Lives'%(time,date)).execute()

    print (created_event['id'])
if __name__ == '__main__':
    main()
