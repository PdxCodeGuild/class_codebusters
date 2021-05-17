
# Define the following functions:

#import random

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# for i in range(21):
#     data.append(random.randint(1, 9))
#     print(i, data[i])
# print(data)

# peaks(data) - Returns the indices of peaks. A peak has a lower number on both the left and the right.


def peaks(data):
    peak = []
    for i in range(1, len(data)-1):
        left = data[i-1]
        middle = data[i]
        right = data[i+1]
        if left < middle and right < middle:
            peak.append(i)
    return peak


# valleys(data) - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.


def valleys(data):
    valley = []
    for i in range(1, len(data)-1):
        left = data[i-1]
        middle = data[i]
        right = data[i+1]
        if left > middle and right > middle:
            valley.append(i)
    return valley


# print(peaks(data))
# print(valleys(data))


# peaks_and_valleys(data) - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

peaks_and_valleys = peaks(data) + valleys(data)
peaks_and_valleys.sort()

print(peaks(data))
print(valleys(data))
print(peaks_and_valleys)
