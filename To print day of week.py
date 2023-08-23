#To print day of week

from datetime import datetime
def dayofweek(d,m,y):
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    return days[datetime(y,m,d).weekday()]
dd=int(input())
mm=int(input())
yy=int(input())
print(dayofweek(dd,mm,yy))
