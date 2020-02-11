# here we are going to see the date and time in utc format
# with the help of pytz library and convert a naive time into desired time zone

# First import datetime and pytz library
import datetime
import pytz

# UTC timezone : dates and time
dt = datetime.datetime(2020,2,11,12,29,30,1000)
dt_utc =  datetime.datetime(2020,2,11,12,29,30,1000,tzinfo = pytz.UTC)

print(dt)
print(dt_utc)

print("*"*50)



# Conversion of navie datetime to desired UTC time zone with pytz

# naive date time
naive_dt = datetime.datetime.now(tz = pytz.UTC)

# Asia/Kolkata UTC timezone
asia_kolkata  = naive_dt.astimezone(pytz.timezone('Asia/Kolkata'))

print(naive_dt)
print(asia_kolkata)

print("*"*50)


# All the UTC TimeZone Names available in the pytz library
# All time Zones available in pytz library
# for tz in pytz.all_timezones:
#     print(tz)
