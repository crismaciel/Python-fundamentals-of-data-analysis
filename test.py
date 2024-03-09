from datetime import datetime
import calendar

# get current datetime
dt = datetime.now()
print('Datetime is:', dt)

# weekday (Monday =0 Sunday=6)
print('Weekday Number:', dt.weekday())

# isoweekday(Monday =1 Sunday=6)
print('ISO Weekday Number:', dt.isoweekday())

# get weekday name
print('Weekday Name:', dt.strftime('%A'))

# get day name
x = calendar.day_name[dt.weekday()]
print('Weekday name is:', x)