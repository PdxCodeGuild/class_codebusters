from datetime import datetime
today = datetime.now()


# Datetime properties
today.year
today.month
today.day
today.hour
today.minute
today.second
today.microsecond

# tomorrow = datetime(2021, 5, 25, 14, 30, 0)
# print(tomorrow)

# date = "May 24, 2021"
# current_date = datetime.strptime(date, "%B %d, %Y")

# date = "25MAR2021"
# current_date = datetime.strptime(date, "%d%b%Y")

# string_date = current_date.strftime("%B %d, %Y")

today = datetime.now()

print(today.strftime("%m/%d/%y"))
