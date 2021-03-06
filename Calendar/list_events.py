from pprint import pprint
import Google


def get_item_summary(cID):
    CLIENT_SECRET_FILE = 'client_secret.json'
    API_NAME = 'calendar'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    service = Google.Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    page_token = None
    while True:
        events = service.events().list(calendarId=cID, pageToken=page_token).execute()
        return events['items'][0]
        pprint(events['items'][0])
        for event in events['items']:
            pprint(event.get('summary'))
        page_token = events.get('nextPageToken')
        if not page_token:
            break
