"""
Peaks and Valleys
Define the following functions:

peaks(data) - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys(data) - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

peaks_and_valleys(data) - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
"""
import random

# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# data = [9, 7, 6, 3, 10, 20, 20, 20, 1, 2, 3, 4]
data = [random.randint(1, 20) for _ in range(21)]


def peaks(data):
    peaks_list = []
    for i in range(1, len(data) - 1):
        item = data[i]
        if item > data[i-1] and item > data[i+1]:
            peaks_list.append(i)
    return peaks_list


def valleys(data):
    peaks_list = []
    for i in range(1, len(data) - 1):
        item = data[i]
        if item < data[i-1] and item < data[i+1]:
            peaks_list.append(i)
    return peaks_list


def peaks_and_valleys(data):
    peaks_list = peaks(data)
    valleys_list = valleys(data)
    return sorted(peaks_list + valleys_list)


"""
Version 2 (optional)
Using the data list above, draw the image of X's above.
"""

max_count = 0
max_numbers = []
mountains = []
while max_count != max(data):
    vertical = []
    for num in data:
        if num == max(data) - max_count or num in max_numbers:
            vertical.append('x ')
            max_numbers.append(num)
        else:
            vertical.append('  ')
    max_count += 1
    mountains.append(vertical)


"""
Version 3 (optional)
Imagine pouring water into onto these hills. The water would wash off the left and right sides, but would accumulate in the valleys. Below the water is represented by O's. Given data, calculate the amount of water that would be collected, and if you can, draw the following diagram.
"""

for row in mountains:
    for i in range(len(row)):
        left = row[:i]
        right = row[i:]
        if row[i] == "  ":
            if "x " in left and "x " in right:
                row[i] = "o "


peaks_indices = peaks(data)
valleys_indices = valleys(data)
water_data = []
for x, y in zip(peaks_indices, valleys_indices):
    height = data[x] - data[y]
    half_base = y - x
    area = half_base * height
    water_data.append(area)


for row in mountains:
    print("".join(row))
print(water_data)
