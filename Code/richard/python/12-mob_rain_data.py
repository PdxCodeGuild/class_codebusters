# Part 1
# Go to http://or.water.usgs.gov/non-usgs/bes/ and select a data table. Copy the contents and save them into your own rain_data.txt. The two columns that are most important are the date and the daily total. The simplest representation of this data is a list of tuples, but you may also use a list of dictionaries. Hint: Use regular expressions to find relevant data.

import requests,re,math
from datetime import datetime
response = requests.get('https://or.water.usgs.gov/non-usgs/bes/simmons.rain')
response.encoding = 'utf-8'

# print(response.text)

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
result = response.text
result = re.findall(r'(\d{2}-\w{3}-\d{4})\s+(\d+)',result)
# print(result)

def average(x):
    total = 0
    for i in range(len(x)):
        total += int(x[i][1])
    return total / len(x)
# average_result = average(result)

def variance(x):
    mu = average(x)
    total = 0
    for i in range(len(x)):
        total += (int(x[i][1]) - mu)**2
    return total / len(x)
# print(variance(result))

def standard_deviation(x):
    v = variance(x)
    return math.sqrt(v)
# print(standard_deviation(result))

def getMaxRainFall(resultsList):
    max_date = datetime.now()
    max_rainfall = 0
    for i in range(len(resultsList)):
        if int(resultsList[i][1]) > max_rainfall:
            max_rainfall = int(resultsList[i][1])
            max_date = resultsList[i][0]
    return (max_date,max_rainfall)
max_rain_date = getMaxRainFall(result)

# print(f"The max rainfall is {max_rain_date[1] * .01:.2f} inches on {max_rain_date[0]}.")

def change_to_datetime(result):
    convertedResult = []
    for i in range(len(result)):
        convertedResult.append((datetime.strptime(result[i][0],'%d-%b-%Y'),int(result[i][1])))
    return convertedResult
convertedList = change_to_datetime(result)

def combine_by_month(resultList):
    resultDict = {}
    for i in range(len(resultList)):
        curent_year_month = f"{resultList[i][0].year}-{resultList[i][0].month}"
        if curent_year_month in resultDict:
            resultDict[curent_year_month] += resultList[i][1]
        else:
            resultDict[curent_year_month] = resultList[i][1]
    
    return [(k,v) for k,v in resultDict.items()]

def combine_by_year(resultList):
    resultDict = {}
    for i in range(len(resultList)):
        curent_year = f"{resultList[i][0].year}"
        if curent_year in resultDict:
            resultDict[curent_year] += resultList[i][1]
        else:
            resultDict[curent_year] = resultList[i][1]
    
    return [(k,v) for k,v in resultDict.items()]

combinedList = combine_by_year(convertedList)
print(getMaxRainFall(combinedList))