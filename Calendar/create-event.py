from pprint import pprint
from Google import Create_Service, convert_to_RFC_datetime


CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# hour_adjustment
event = {
  'summary': 'Interview SDE I',
  'location': '800 Howard St., San Francisco, CA 94103',
  'description': 'A chance to hear more about Google\'s developer products.',
  'start': {
    'dateTime': convert_to_RFC_datetime(2021,3,6,9,0),
    'timeZone': 'America/Los_Angeles',
  },
  'end': {
    'dateTime': convert_to_RFC_datetime(2021,3,6,13,0),
    'timeZone': 'America/Los_Angeles',
  },
  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=2'
  ],
  'attendees': [
    {'email': 'prithviraj.ext@grofers.com'},
    {'email': 'siddhart.ext@grofers.com'},
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}
event = service.events().insert(calendarId='2889545659ube7r0ip0qb9ptjs@group.calendar.google.com', body=event).execute()
print('Event created: %s' % (event.get('htmlLink')))