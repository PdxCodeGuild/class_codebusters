'''
The 'City of Portland Bureau of Environmental Services' operates and maintains a network of rain gauges around Portland, and publishes their data publicly: http://or.water.usgs.gov/non-usgs/bes/. The data tables available on the site look something like...

Daily  Hourly data -->

   Date     Total    0   1
--------------------------
25-MAR-2016     0    0   0
24-MAR-2016     6    0   1
23-MAR-2016     -    -   -
MORE...
Part 1
Go to http://or.water.usgs.gov/non-usgs/bes/ and select a data table. Copy the contents and save them into your own rain_data.txt. The two columns that are most important are the date and the daily total. The simplest representation of this data is a list of tuples, but you may also use a list of dictionaries. Hint: Use regular expressions to find relevant data.

with open('hayden_island.rain', 'r') as file:
    text = file.read()
print(text)
To parse the dates, use datetime.strptime. This allows for easy access to the year, month, and day as ints. Below I've shown how to parse an example string, resulting in a datetime object. We can then access the year, month, and day on that datetime as ints. Later, if you want to print the datetime in a more human-readable format, you can use datetime.strftime.

from datetime import datetime

# turn a string into a datetime object
date = datetime.strptime('25-MAR-2016', '%d-%b-%Y')

# access the properties of that object
print(date.year)   # 2016
print(date.month)  # 3
print(date.day)    # 25
print(date)  # 2016-03-25 00:00:00

# turn the datetime object back into a string
print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016
Part 2
Now that you've successfully extracted the data, let's calculate some statistics.

1. Calculate the Mean
The mean is the sum of all the daily totals divided by the number of daily totals. The sigma in this fomula represents a sum of all the values in the list.

mean

def average(x):
    total = 0
    for i in range(len(x)):
        total += x[i]
    return total / len(x)
print(average([34, 56, 73, 21])) # 46.0
2. Calculate the Variance
Use the mean to calculate the variance, which is a measure of how "spread out" the data is:

standard_deviation

def variance(x):
    mu = average(x)
    total = 0
    for i in range(len(x)):
        total += (x[i] - mu)**2
    return total / len(x)
print(variance([34, 56, 73, 21])) # 399.5
The standard deviation is the square root of the variance. 68.2% of the data falls within 1 standard deviation of the mean.

bell_curve

import math
def standard_deviation(x):
    v = variance(x)
    return math.sqrt(v)
print(standard_deviation([34, 56, 73, 21])) # 19.987
3. Find the day which had the most rain.
Loop over all the records to find the one which had the most rain, print out the date and daily total to the user.
'''

import re
from math import sqrt

with open('rain_table.txt', 'r') as file:
    raw_data = file.read()

rain_data = [data for data in re.findall(r'\d{2}-\w{3}-\d{4}   ? ?\d+', raw_data)]

rain_dicts = [{'date': data[:11:], 'rain': int(data[15::])} for data in rain_data]

c = 0
rain_count = 0
for d in rain_dicts:
    rain_count += d['rain']
    c += 1
mean = round(rain_count / c, 4)

c1 = 0
rain_count1 = 0
for d in rain_dicts:
    rain_count1 += (d['rain'] - mean) ** 2
    c1 += 1
variance = round(rain_count1 / c1, 4)

strd_deviation = round(sqrt(variance), 4)

date = []
rain = []
for d in rain_dicts:
    date.append(d['date'])
    rain.append(d['rain'])
most_rain = max(rain)
date_rain = date[rain.index(most_rain)]

print(f'''
The average rainfall was {mean}.
The variance was {variance}.
The standard deviation was {strd_deviation}.
{date_rain} had the maximum amount of rain at {most_rain} tips.
''')