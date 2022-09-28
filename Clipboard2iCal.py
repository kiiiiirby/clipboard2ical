import os
import re
from pathlib import Path
from datetime import datetime
from icalendar import Calendar, Event
from pyperclip import waitForNewPaste

# init the calendar
cal = Calendar()

# Some properties are required to be compliant
cal.add('prodid', '-//Clipboard To iCal//https://github.com/kiiiiirby/clipboard2ical//')
cal.add('version', '2.0')

print("""
|-------------------------------------------|
|              Clipboard2iCal               |
|      Export clipboard to iCal file.       |
|                                           |
|https://github.com/kiiiiirby/clipboard2ical|
|-------------------------------------------|
""")

input("\nPress Enter to continue...")

check = ''
while check.upper() != 'N':

# pyperclip (wait until clipboard updates)
    print("\nPlease copy your timetable to the clipboard.")
    clipboardText = waitForNewPaste(60)  # 60 seconds timeout

# regexs
    typeOfClassRegex = re.compile(r'(Tutorial|Lecture)')
    subjectCodeRegex = re.compile(r'^\w\w\w\w\s\d\d\d')
    timeRegex = re.compile(r'\w+\s\d+:\d+\w+\s-\s\d+:\d+\w+')
    locationRegex = re.compile(r'HQ BLK \w\s\w+\s\S+')
    dateRegex = re.compile(r'\d+\/\d+\/\d+ - \d+\/\d+\/\d+')

# run regexs
    typeOfClass = typeOfClassRegex.findall(clipboardText)
    subjectCode = subjectCodeRegex.findall(clipboardText)
    time = timeRegex.findall(clipboardText)
    classLocation = locationRegex.findall(clipboardText)
    date = dateRegex.findall(clipboardText)

# if subject code not found
    if len(subjectCode) == 0:
        inputSC = input("\nPlease enter the subject code: ")
        subjectCode.insert(0, inputSC)

# print output
    print('\n' + subjectCode[0] + "  " + typeOfClass[0])
    print('\n' + "Time" + '\t ' + "Location" + '\t ' + "Date")

    for i in range(len(time)):
        print(time[i] + '\t ' + classLocation[i] + '\t ' + date[i])
# slice date
        year = int(date[i][6:10])
        month = int(date[i][3:5])
        day = int(date[i][0:2])
# slice time
        startEndTimeRegex = re.compile(r'\d+:\d\d\w\w')
        startEndTime = startEndTimeRegex.findall(time[i])
        startTimeIn = datetime.strptime(startEndTime[0], "%I:%M%p")
        startTimeOut = datetime.strftime(startTimeIn, "%H:%M")
        endTimeIn = datetime.strptime(startEndTime[1], "%I:%M%p")
        endTimeOut = datetime.strftime(endTimeIn, "%H:%M")
# Add calendar subcomponents
        event = Event()
        event.add('summary', subjectCode[0] + " " + typeOfClass[0])
        event.add('dtstart', datetime(year, month, day, int(startTimeOut[0:2]), 0, 0))
        event.add('dtend', datetime(year, month, day, int(endTimeOut[0:2]), 0, 0))
        event.add('location', classLocation)
# Add the event to the calendar
        cal.add_component(event)

    check = input("\nAdd another timetable? (Y/N): ")

# Write to disk
fileName = input("\nName of new iCal file (without extension): ")
directory = Path.cwd() / 'Clipboard2iCal'
try:
    directory.mkdir(parents=True, exist_ok=False)
except FileExistsError:
    print("\nFolder already exists")
else:
    print("\nFolder was created")
print("\nThe file will be saved in " + str(Path.cwd()) + "\Clipboard2iCal")

f = open(os.path.join(directory, fileName+'.ics'), 'wb')
f.write(cal.to_ical())
f.close()

input("Press Enter to close...")

