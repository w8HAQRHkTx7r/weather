import datetime
from pprint import pprint

def getDate(unix_time):
    # Convert the Unix timestamp to a datetime object
    date_obj = datetime.datetime.fromtimestamp(unix_time)

    # Get the month name, day number, and day of the week name
    month = date_obj.strftime('%B')
    day = date_obj.strftime('%d')
    day_of_week = date_obj.strftime('%A')

    # Return a tuple containing the month, day, and day of the week
    return (month, day, day_of_week)

from secrets import APIKEY

import requests
import json

cities = [						#{"city" : "Naperville", "lat" : 41.740289, "lon" : -88.099522},
          {"city" : "Lisboa",     "lat" : 38.71,     "lon" : -9.14     },
          {"city" : "Evora",      "lat" : 38.57,     "lon" : -7.91     },
          {"city" : "Carmona",    "lat" : 37.470915, "lon" : -5.648573 },
          {"city" : "Ronda",      "lat" : 36.743917, "lon" : -5.162285 },
          {"city" : "Ubeda",      "lat" : 38.014979, "lon" : -3.371276 },
          {"city" : "Marid",      "lat" : 40.410688, "lon" : -3.718344 },
          {"city" : "Barcelona",  "lat" : 41.402369, "lon" : 2.171505  },
         ]


UNITS    = "imperial"
EXCLUDES = "minutely,hourly" #,alerts"

for c in cities:
	print("")
	print(c['city'])
	lat = c['lat']
	lon = c['lon']

	url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={EXCLUDES}&units={UNITS}&appid=" + APIKEY
	response = requests.get(url)
	if response.status_code != 200:
		print("Bad status: ", response.status_code)
	j = json.loads(response.text)
#	pprint(j)

	print(f"Currently: {j['current']['temp']:0.2f} {j['current']['weather'][0]['main']}")
	for day_index in range(5):
		d = j['daily'][day_index]
		mon,day,dow = getDate(d['dt'])

		print(f"{mon} {day} {dow[:3]} {d['temp']['min']:.2f} - {d['temp']['max']:0.2f} {d['weather'][0]['main']}")

