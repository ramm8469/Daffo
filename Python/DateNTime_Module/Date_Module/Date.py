import datetime

# Here we are going to see the default(naive) date demo in python
# creating a date
date_ = datetime.date(2020,2,12)
print(date_)

print("*"*50)
# ttting the date by default
date_default = datetime.date.today()
print(date_default)

# getting the today in local time zone
tday = datetime.date.today() 
wkday = datetime.date(2020,2,12).weekday()
# year = datetime.date.year()

print("Today  : ",tday," WeekDay : ",wkday )



# TimeDelta : TimeDelta is just the difference between two dates

tdelta = datetime.timedelta(weeks=52)
res = tday - tdelta
ttdelta = datetime.timedelta(weeks=4*4)
res2 = res - ttdelta
tttdelta = datetime.timedelta(days=2)
res3 = res2 - tttdelta
print(res)
print(res2)
print(res3)

# after_tday = tday+tdelta
# print(after_tday)
# before_tday  = tday - tdelta
# print(before_tday) # date as result


# print(after_tday-before_tday) # (timedelta) days as a result

# Note : if we add/sub date with timedelta, then we get date as a result
# whereas, if we add/sub date with date, then we get days as a result
