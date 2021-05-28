# Part 1
# Go to http://or.water.usgs.gov/non-usgs/bes/ and select a data table. Copy the contents and save them into your own rain_data.txt. The two columns that are most important are the date and the daily total. The simplest representation of this data is a list of tuples, but you may also use a list of dictionaries.


# To parse the dates, use datetime.strptime. This allows for easy access to the year, month, and day as ints. Below I've shown how to parse an example string, resulting in a datetime object. We can then access the year, month, and day on that datetime as ints. Later, if you want to print the datetime in a more human-readable format, you can use datetime.strftime.

# from datetime import datetime

# # turn a string into a datetime object
# date = datetime.strptime('25-MAR-2016', '%d-%b-%Y')

# # access the properties of that object
# print(date.year)   # 2016
# print(date.month)  # 3
# print(date.day)    # 25
# print(date)  # 2016-03-25 00:00:00

# # turn the datetime object back into a string
# print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016

import re

with open('rain-table.txt', 'r') as file:
    raw_data = file.read()
# print(text)

whole_rain_data = [data for data in re.findall(r'\d{2}-.{3}-\d{4}     ?\d+', raw_data)] 
# lets remove all the noise and bring it down to '20-MAY-2021    11'

processed_rain_data = [{'date':  data[:11:], 'rain':  data[15::]} for data in whole_rain_data]
# now lets process this into more finite data, [{date: XYZ, rain: xyz}]



# Part 2
# Now that you've successfully extracted the data, let's calculate some statistics.

# Calculate the Mean
# The mean is the sum of all the daily totals divided by the number of daily totals. The sigma in this fomula represents a sum of all the values in the list.

# print(processed_rain_data['rain'])
mean_rain = sum([int(rain_level['rain']) for rain_level in processed_rain_data])/len(processed_rain_data)
deviation = sum([int(rain_level['rain'])-mean_rain for rain_level in processed_rain_data])/len(processed_rain_data)**2
print(mean_rain, deviation)
