from pprint import pprint
import Calendar.Google as Google
import os
from datetime import datetime


def get_events(event_id):
    current_path = os.path.dirname('client_secret.json')
    print("PATHH ", current_path)
    CLIENT_SECRET_FILE = "Calendar/client_secret.json"
    API_NAME = 'calendar'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    service = Google.Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    page_token = None
    while True:
        events = service.events().list(calendarId='primary', pageToken=page_token,
                                       timeMin=Google.convert_to_RFC_datetime(2021, 3, 6, 0, 0),
                                       timeMax=Google.convert_to_RFC_datetime(2021, 3, 6, 23, 59)).execute()
        pprint(events)
        return events['items']  # Returns events of the day
