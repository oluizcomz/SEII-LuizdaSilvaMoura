import datetime
import pytz

print('date: ',datetime.date(2021, 3, 16))

tday = datetime.date.today()
print('dat actual: ',tday.day )

tdelta = datetime.timedelta(hours=12)


bday = datetime.date(2016, 9, 24)

till_bday = bday - tday

print('diferença entre as datas em dias: ',till_bday.days)

t = datetime.time(9, 30, 45, 100000)
print(t)
