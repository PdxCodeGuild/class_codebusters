"""

Define the following functions:

peaks(data) - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys(data) - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

peaks_and_valleys(data) - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

"""
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def peaks(data):
    peak = []
    for i in range(1, len(data) - 1):
        item = data[i]
        if item > data[i-1] and item > data[i + 1]:
            peak.append(i)
    return peak


"""
    for num in data:
        if num > data[data.index(num) + 1] and num > data[data.index(num) - 1]:
            peak.append(data.index(num))

    return peak"""


def valleys(data):
    valley = []
    for i in range(1, len(data) - 1):
        item = data[i]
        if item < data[i-1] and item < data[i + 1]:
            valley.append(i)
    return valley


"""    
    
    for num in data:
        if num < data[data.index(num) + 1] and num < data[data.index(num) - 1]:
            valley.append(data.index(num))

    return valley

"""


def peaks_and_valleys(data):
    both = []
    both.extend(peaks(data))
    both.extend(valleys(data))
    return sorted(both)


print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))
