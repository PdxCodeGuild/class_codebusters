#-----------------------------------------------#
'''
PDX Code Guild
Class CodeBusters
Week 04
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
Version 1: 
Version 2: 
Version 3: 

Future Improvements:

- 

'''

#-----------------------------------------------#
# Import Dependencies
#-----------------------------------------------#



#-----------------------------------------------#
# Define Functions
#-----------------------------------------------#

def peaks (data):
    result_peaks = []
    for i in range(len(data)):
        if i == 0:
            continue
        elif data[i-1] < data[i] < data[i+1]:
            result_peaks.append(data[i])
    return result_peaks

def valleys (data):

    return

def peaks_and_valleys (data):

    return

