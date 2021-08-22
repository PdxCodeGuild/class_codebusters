#-----------------------------------------------#
'''
PDX Code Guild
Class CodeBusters
Lab 07 - Peaks and Valleys
Jared Nistler
'''
#-----------------------------------------------#
# Instructions
#-----------------------------------------------#
'''
Define the following functions:

- peaks(data) - Returns the indices of peaks. A peak has a lower 
number on both the left and the right.

- valleys(data) - Returns the indices of 'valleys'. A valley is 
a number with a higher number on both the left and the right.

- peaks_and_valleys(data) - uses the above two functions to compile 
a single list of the peaks and valleys in order of appearance in 
the original data.

'''
#-----------------------------------------------#
# Developer Notes
#-----------------------------------------------#
'''
Version 1: Complete
Version 2: 
Version 3: 

Future Improvements:

- 

'''

#-----------------------------------------------#
# Import Dependencies
#-----------------------------------------------#

#-----------------------------------------------#
# Define Constants
#-----------------------------------------------#

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

#-----------------------------------------------#
# Define Functions
#-----------------------------------------------#

# Returns the indices of peaks. A peak has a lower 
# number on both the left and the right.
def peaks (data):
    # Define list in which to store indicies of peaks
    index_list = []

    # Iterates through the data list, checks if each data point is greater than
    # the two data points on either side of it, and if so, adds it to the peak list
    for i in range(1, len(data) - 1):
        data_point = data[i]
        if data_point > data[i+1] and data_point > data[i-1]:
            index_list.append(i)
    return index_list

# Returns the indices of 'valleys'. A valley is a 
# number with a higher number on both the left and 
# the right.
def valleys (data):
    # Define list in which to store indicies of valleys
    index_list = []

    # Iterates through the data list, checks if each data point is less than
    # the two data points on either side of it, and if so, adds it to the valley list
    for i in range(1, len(data) - 1):
        data_point = data[i]
        if data_point < data[i+1] and data_point < data[i-1]:
            index_list.append(i)
    return index_list

# uses the above two functions to compile a single 
# list of the peaks and valleys in order of appearance 
# in the original data.
def peaks_and_valleys (data):
    peak_list = peaks(data)
    valley_list = valleys(data)
    return_list = peak_list + valley_list
    return_list.sort()
    return return_list

print(peaks_and_valleys(data))