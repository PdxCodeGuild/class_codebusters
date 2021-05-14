"""
Peaks and Valleys

Define the following functions:

    peaks(data) - Returns the indices of peaks. A peak has a lower number on both the left 
    and the right.

    valleys(data) - Returns the indices of 'valleys'. A valley is a number with 
    a higher number on both the left and the right.

    peaks_and_valleys(data) - uses the above two functions to compile a single 
    list of the peaks and valleys in order of appearance in the original data.

    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peaks(data) # [6, 14]
valleys(data) # [9, 17]
peaks_and_valleys(data) # [6, 9, 14, 17]
"""

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def peaks(data):
    peak = []
    for i in range(1, len(data)-1):
        if data[i - 1] < data[i] and data[i] > data[i + 1]:
            peak.append(i)
    return f'peaks {peak}'


def valleys(data):
    valley = []
    for i in range(1, len(data)-1):
        if data[i - 1] > data[i] and data[i] < data[i + 1]:
            valley.append(i)
    return f'valleys {valley}'


def peaks_and_valleys(data):
    peak_and_valley = []
    for i in range(1, len(data)-1):
        if data[i - 1] > data[i] and data[i] < data[i + 1] \
                or data[i - 1] < data[i] and data[i] > data[i + 1]:
            peak_and_valley.append(i)
    return f'peaks_and valleys {peak_and_valley}'


print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))
