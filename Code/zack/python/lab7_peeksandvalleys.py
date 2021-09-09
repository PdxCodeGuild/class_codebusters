"""
Define the following functions:

peaks(data) - Returns the indices of peaks. 
A peak has a lower number on both the left and the right.

valleys(data) - Returns the indices of 'valleys'. 
A valley is a number with a higher number on both the left and the right.

peaks_and_valleys(data) - uses the above two functions to compile 
a single list of the peaks and valleys in order of appearance 
in the original data.

"""
# index 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def peaks(nums):
    peak = []
    for i in range(1, len(nums)-1):
        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
            peak.append(nums[i])
    return peak

# print(peaks(data))




def valleys(nums):
    valley = []
    for i in range(1, len(nums)-1):
        if nums[i] < nums[i-1] and nums[i] < nums[i+1]:
            valley.append(nums[i])
    return valley

  



def peaks_and_valleys(nums):
    ps_and_vs = []
    for i in range(1, len(nums)-1):
        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
            ps_and_vs.append(nums[i])
        if nums[i] < nums[i-1] and nums[i] < nums[i+1]:
            ps_and_vs.append(nums[i])
    return sorted(ps_and_vs)            








'''
DISCLAIMER
was stuck on: 
data[i] > data[i-1] and data[i] data[i+1]
I had:
data[i] > data[i-1] and data[i+1]
'''