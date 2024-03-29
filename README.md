# Clipboard2iCal
<img src="https://img.shields.io/github/license/haubinhui/clipboard2ical">
Written for the timetable format of Singapore Institute of Management in SIMConnect. Takes the list format of the timetable and
output a iCalender file, ready to be imported to your calender of choice.


<img src="https://onesim-prod.s3.ap-southeast-1.amazonaws.com/onesim/media/ge-sim-ge/simgelogo.png" width="250">

## How It's Made:

**Tech used:** Python

Makes use of the [iCalendar](https://pypi.org/project/icalendar/) to create iCalendar events and [Pyperclip](https://pypi.org/project/pyperclip/) to collect clipboard input.

## Example:
This is an example of a timetable format found on SIMConnect.

**CSIT 115 - Data Management & Security**
| Class Nbr | Section | Component | Days & Times | Room | Start/End Date |
| --- | --- | --- | --- | --- | --- |
| 1753 | T06 | Tutorial  | Th 12:00PM - 3:00PM | HQ BLK A LAB A.5.14/A.5.15 | 06/10/2021 - 06/10/2021 |
|  |  |   | Mo 8:30AM - 11:30AM | HQ BLK A LAB A.5.14/A.5.15 | 03/10/2021 - 03/10/2021 |
|  |  |   | Tu 8:30AM - 11:30AM | HQ BLK A LAB A.5.14/A.5.15 | 04/10/2021 - 04/10/2021 |
|  |  |   | Th 12:00PM - 3:00PM | HQ BLK A LAB A.5.14/A.5.15 | 10/11/2021 - 10/11/2021 |

## Usage:
When prompted, copy the timetable from SIMConnect onto your clipboard. Enter the desired name of the created iCalendar file and import it into your calendar of choice.

<img src="https://github.com/haubinhui/clipboard2ical/blob/main/Screenshot.png?raw=true">
