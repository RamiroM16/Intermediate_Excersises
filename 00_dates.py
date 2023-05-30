### Dates ###

from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

now = datetime.now()
def print_date(date):
    print("Año", date.year)
    print("Mes", date.month)
    print("Dia", date.day)
    print("Hora ", date.hour)
    print("Minuto", date.minute)
    print("Segundo", date.second)
    print("Timestamp", date.timestamp())


print_date(now)



year_2023 = datetime(2023,5,3)

print_date(year_2023)

current_time = time(21,6,0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

current_date = date.today()
print (current_date.year)
print (current_date.month)
print (current_date.day)
print (current_date.weekday())

current_date = date(2022,10,6)
print (current_date.year)
print (current_date.month)
print (current_date.day)


diff = year_2023 - now
print(diff)
diff = year_2023.date() - current_date
print(diff)


time_delta = timedelta(200,100,100, weeks=10)
endtime_delta = timedelta(300,100,100, weeks=13)

print(endtime_delta - time_delta)
print(endtime_delta + time_delta)