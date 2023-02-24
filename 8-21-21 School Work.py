import datetime
import datetime as dt
help(dt)
print(dir(dt.date.today()))
print(dt.date.today().month,dt.date.today().day,dt.date.today().year)
print(dt.date.today())
print(dt.datetime.today())

nowTime = dt.datetime.today()
print(nowTime)
td = dt.timedelta(days=30)
print(nowTime + td)

print(td.total_seconds())