from pprint import pprint
from Calendar.Google import Create_Service, convert_to_RFC_datetime


def create_event():
    CLIENT_SECRET_FILE = 'Calendar/client_secret.json'
    API_NAME = 'calendar'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    # hour_adjustment
    event = {
      'summary': 'Interview SDE I',
      'location': 'Remote',
      'description': 'Interview for SDE I position',
      'start': {
        'dateTime': convert_to_RFC_datetime(2021, 3, 7, 13, 30),
        'timeZone': 'Asia/Kolkata',
      },
      'end': {
        'dateTime': convert_to_RFC_datetime(2021, 3, 7, 14, 30),
        'timeZone': 'Asia/Kolkata',
      },
      'attendees': [
        {'email': 'siddharth.ext@grofers.com'},
      ],
      'reminders': {
        'useDefault': False,
        'overrides': [
          {'method': 'email', 'minutes': 24 * 60},
          {'method': 'popup', 'minutes': 10},
        ],
      },
    }
    event = service.events().insert(calendarId='prithviraj.ext@grofers.com', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))
