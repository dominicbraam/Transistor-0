# Google Cal Handler
# Help:
# - https://karenapp.io/articles/how-to-automate-google-calendar-with-python-using-the-calendar-api/
# - https://qxf2.com/blog/google-calendar-python/

from cal_init import get_calendar_service
from dateutil.parser import parse as dtparse
from datetime import datetime
from os import getenv

def get_events(date):

    year = int(datetime.strftime(date, format='%Y'))
    month = int(datetime.strftime(date, format='%m'))
    day = int(datetime.strftime(date, format='%d'))
    start_date = datetime(year, month, day, 0, 0, 0, 0).isoformat() + 'Z'
    end_date = datetime(year, month, day, 23, 59, 59, 0).isoformat() + 'Z'

    service = get_calendar_service()

    # calendar_id = "dominic.braam@gmail.com"
    calendar_id = getenv('CAL_ID')
    # print('\n----%s:\n' % calendar_id)
    eventsResult = service.events().list(
        calendarId=calendar_id,
        timeMin=start_date,
        timeMax=end_date,
        singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])
    return events
