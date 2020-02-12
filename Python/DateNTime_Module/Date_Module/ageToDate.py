import datetime

def age_To_Date(age,month,days):
    final_days = 0
    final_days += (age*365.2425)
    final_days += (month*30)
    final_days += days
    print(final_days)

    time_delta_created = datetime.timedelta(days=final_days)
    td = datetime.date.today()

    final_date = td  - time_delta_created

    return final_date


# today = datetime.date.today()
# print(today)
# date_created = datetime.date(1997,9,9)
# print(date_created)
# time_delta = datetime.timedelta(weeks=1)
# print(today-time_delta) # date
# time_delta_recieved = today-date_created
# # years = time_delta_recieved/365
# # months = years/12
# # days = months/20
# # print(time_delta_recieved) # time_delta
# # print("Y : ",years," M : ",months," D : ",days)

# print(time_delta_recieved)
# print(today-time_delta_recieved)

# time_delta_created  = datetime.timedelta(days=365)
# print(today-time_delta_created)

print(age_To_Date(1,1,0))
