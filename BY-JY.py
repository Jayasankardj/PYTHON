#JY-BY

from datetime import datetime
from dateutil import relativedelta

d1=input("Enter date: ")
d2=input("Enter date: ")

start_date=datetime.strptime(d1,"%d/%m%/%y")
end_date=datetime.strptime(d2,"%d/%m%,/%y")

delta=relativedelta.relativedelta(end_date,start_date)
print('Years, Months, Days between two dates is')
print(delta.years,"Years",delta.months,"Months",delta.dates,"Days")

delta.years
d3=d1.split('/')
by=d3[2]
d4=d2.split('/')
jy=d3[2]

if delta.years>=19 and by%4==0:
    print("I am lucky adult")
elif delta.years<19:
    print("I am aspiring to become adult")

if by%400==0 or by%100!=0 and by%4==0:
    print("Birth year is leap year")
else:
    print("Birth year is not a leap year")

if jy%400==0 or jy%100!=0 and jy%4==0:
    print("Birth year is leap year")
else:
    print("Birth year is not a leap year")

