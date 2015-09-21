import urllib
import json
import datetime

from config import EVENTBRITE

class EventbriteAPI(object):
	def __init__(self, config=EVENTBRITE):
		self.token = config['token']

	def create_event(self, name, start_time, end_time, start_timezone="America/New_York", end_timezone="America/New_York", currency="USD"):
		url = "https://www.eventbriteapi.com/v3/events/?token=%s"%self.token
		request_params = {
		    "event.name.html": name,
		    "event.start.timezone": start_timezone,
		    "event.end.timezone": end_timezone,
		    "event.start.utc": start_time,
		    "event.end.utc": end_time,
		    "event.currency": currency
		}
		response = json.loads(urllib.urlopen(url, data=urllib.urlencode(request_params)).read())
		return response
