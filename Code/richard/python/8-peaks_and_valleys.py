# Peaks and Valleys
# Define the following functions:

# peaks(data) - Returns the indices of peaks. A peak has a lower number on both the left and the 
# right.

# valleys(data) - Returns the indices of 'valleys'. A valley is a number with a higher number on 
# both the left and the right.

# peaks_and_valleys(data) - uses the above two functions to compile a single list of the peaks 
# and valleys in order of appearance in the original data.

def peaks(data):
    peakList = []
    i = 1
    while i < len(data) - 1:
        if data[i] > data[i - 1] and data[i] > data[i + 1]:
            peakList.append(i)
        i += 1
    return peakList

def valleys(data):
    valleyList = []
    i = 1
    while i < len(data) - 1:
        if data[i] < data[i - 1] and data[i] < data[i + 1]:
            valleyList.append(i)
        i += 1
    return valleyList
'''
def peaks_and_valleys(data):
    return peaks(data) + valleys(data)


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print(f"Peaks = {peaks(data)}") # [6, 14]
print(f"Valleys = {valleys(data)}") # [9, 17]
print(f"Peaks and Valleys = {peaks_and_valleys(data)}") # [6, 9, 14, 17]

# Version 2 (optional)
# Using the data list above, draw the image of X's above.

def loopData(data, num):
    rows = []
    for i in range(len(data)):
        if data[i] > num:
            rows.append('X')
        else:
            rows.append(' ')
    for i in rows:
        print(i, end = '')


def createMountains(data):
    for i in reversed(range(max(data))):
        loopData(data, i)
        print()

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
createMountains(data)
'''
# Version 3 (optional)
# Imagine pouring water into onto these hills. The water would wash off the left and right sides,
# but would accumulate in the valleys. Below the water is represented by O's. Given data, 
# calculate the amount of water that would be collected, and if you can, draw the following diagram.



data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

peak = peaks(data)
valley = valleys(data)

def loopData(data, num,peak,valley):
    rows = []
    j = 0
    countWater = 0
    for i in range(len(data)):
        if (j + 1 < len(peak)) and (i > (valley[j] - peak[j]) + valley[j]):
            j += 1
        if data[i] > num:
            rows.append('X')
        elif (i > peak[j]) and (data[i] < data[peak[j]] > num) and (data[i] <= num):
            rows.append('O')
            countWater += 1
        else:
            rows.append(' ')
        
    for i in rows:
        print(i, end = '')
    return countWater


def createMountains(data):
    waterAmount = 0
    peak = peaks(data)
    valley = valleys(data)
    for i in reversed(range(max(data))):
        waterAmount += loopData(data, i,peak,valley)
        print()
    print(f"Water Amount is {waterAmount}")
createMountains(data)