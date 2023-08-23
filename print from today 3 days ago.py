#print from today 3 days ago

from datetime import datetime
today=datetime.today()
x=today-datetime.timedelta(days=3)
print(x)
print(today)
