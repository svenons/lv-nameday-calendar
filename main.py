import os
from icalendar import Calendar, Event
from datetime import datetime

from contactreader import read_contacts
from datareader import read_data

# Reading the contacts
contacts_file = 'contacts.vcf'
contacts = read_contacts(contacts_file)

names = []
for x in contacts:
    name = x.split(', ')[0]
    names.append(name)

# Reading the name-days
data_folder = os.path.join(os.path.dirname(__file__), 'data') # Get the path to the data folder
data_read = read_data(data_folder, 'name-days-lv-extended.json', 'name-days-lv.json')

calendar_dict = {}

for x in data_read:
    for y in data_read[x]:
        if y in names:
            if x in calendar_dict:
                calendar_dict[x] += ', ' + y
            else:
                calendar_dict[x] = y


cal = Calendar()

for date, names in calendar_dict.items():
    event = Event()
    event.add('summary', names)
    event.add('dtstart', datetime.strptime(date, '%m-%d').date())  # Fix: Convert to date object

    # Set the event to repeat every year
    event.add('rrule', {'freq': 'yearly'})
    event.add('dtstart', datetime.strptime(date, '%m-%d').date())  # Fix: Convert to date object

    cal.add_component(event)

with open('calendar.ics', 'wb') as f:
    f.write(cal.to_ical())

with open('calendar.ics', 'wb') as f:
    f.write(cal.to_ical())



