#Exercise 1: Print current date and time in Python
import datetime
#shows only time
print(datetime.datetime.now().now())

#Solution 2 using time.strftime()
from time import gmtime, strftime
print(strftime("%Y-%m-%d%H:%M:%S", gmtime()))

#Exercise 2: Convert string into a datetime object
from datetime import datetime
date_string = "Feb 25 2020 4:20PM"
datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print(datetime_object)

#Exercise 5: Find the day of the week of a given date
from datetime import datetime
given_date = datetime(2020, 7, 26)
#to get weekday as integer
print(given_date.today().weekday())
#to get the emglish name of the weekday
print(given_date.strftime('%A'))

#Exercise 8: Convert the following datetime into a string
from datetime import datetime

given_date = datetime(2020, 2, 25)
string_date = given_date.strftime("%Y-%m-%d %H:%M:%S")
print(string_date)

#Exercise 9: Calculate the date 4 months from the current date
from datetime import datetime

from dateutil.relativedelta import relativedelta

# 2020-02-25
given_date = datetime(2020, 2, 25).date()

months_to_add = 4
new_date = given_date + relativedelta(months=+ months_to_add)
print(new_date)