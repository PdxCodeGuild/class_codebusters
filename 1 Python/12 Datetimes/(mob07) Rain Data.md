# Rain Data

The 'City of Portland Bureau of Environmental Services' operates and maintains a network of rain gauges around Portland, and publishes their data publicly: http://or.water.usgs.gov/non-usgs/bes/. The data tables available on the site look something like...

```
Daily  Hourly data -->

   Date     Total    0   1
--------------------------
25-MAR-2016     0    0   0
24-MAR-2016     6    0   1
23-MAR-2016     -    -   -
MORE...
```

## Part 1

Go to http://or.water.usgs.gov/non-usgs/bes/ and select a data table. Copy the contents and save them into your own `rain_data.txt`. The two columns that are most important are the date and the daily total. The simplest representation of this data is a list of tuples, but you may also use a list of dictionaries.

```python
with open('hayden_island.rain', 'r') as file:
    text = file.read()
print(text)
```

To parse the dates, use [datetime.strptime](<15 Datetimes.md>). This allows for easy access to the year, month, and day as `int`s. Below I've shown how to parse an example string, resulting in a [datetime](../1%20Python/Datetime.md) object. We can then access the year, month, and day on that datetime as ints. Later, if you want to print the datetime in a more human-readable format, you can use [datetime.strftime](<15 Datetimes.md>).

```python
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
```

## Part 2

Now that you've successfully extracted the data, let's calculate some statistics.

### 1. Calculate the Mean

The mean is the sum of all the daily totals divided by the number of daily totals. The sigma in this fomula represents a sum of all the values in the list.

![mean](https://github.com/PdxCodeGuild/class_eagle/blob/main/1%20Python/labs/images/average.png)

```python
def average(x):
    total = 0
    for i in range(len(x)):
        total += x[i]
    return total / len(x)
print(average([34, 56, 73, 21])) # 46.0
```

### 2. Calculate the Variance

Use the mean to calculate the variance, which is a measure of how "spread out" the data is:

![standard_deviation](https://github.com/PdxCodeGuild/class_eagle/raw/main/1%20Python/labs/images/variance.png)

```python
def variance(x):
    mu = average(x)
    total = 0
    for i in range(len(x)):
        total += (x[i] - mu)**2
    return total / len(x)
print(variance([34, 56, 73, 21])) # 399.5
```

The standard deviation is the square root of the variance. 68.2% of the data falls within 1 standard deviation of the mean.

![bell_curve](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Standard_deviation_diagram.svg/500px-Standard_deviation_diagram.svg.png)

```python
import math
def standard_deviation(x):
    v = variance(x)
    return math.sqrt(v)
print(standard_deviation([34, 56, 73, 21])) # 19.987
```

### 3. Find the day which had the most rain.

Loop over all the records to find the one which had the most rain, print out the date and daily total to the user.
