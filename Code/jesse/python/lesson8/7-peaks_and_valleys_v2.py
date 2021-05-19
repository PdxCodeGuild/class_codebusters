'''
Using the data list above, draw the image of X's above.

Hint 1: If you wanted to draw this horizontally, you could do so very easily like this.

for num in data:
    print('x' * num)
Hint 2: print can only work on one line at a time, so you'll have to loop and decide to either print a space ' ' or an 'X' for every column.
'''

# Returns the indices of peaks. A peak has a lower number on both the left and the right.

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    peak_indices = []
    for i in range(1, len(data) - 1):
        if data[i - 1] < data[i] and data[i + 1] < data[i]:
            peak_indices.append(i)
    return peak_indices

# print(peaks(data))

# Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

def valleys(data):
    valley_indices = []
    for i in range(1, len(data) - 1):
        if data [i - 1] > data[i] and data[i + 1] > data[i]:
            valley_indices.append(i)
    return valley_indices

# print(valleys(data))

# Uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

def peaks_and_valleys(data):
    peak_valley_indices = []
    for i in range(1, len(data) - 1):
        if data[i - 1] < data[i] and data[i + 1] < data[i]:
            peak_valley_indices.append(i)
        elif data [i - 1] > data[i] and data[i + 1] > data[i]:
            peak_valley_indices.append(i)
    return peak_valley_indices

# print(peaks_and_valleys(data))

# draw a graph from "data"
# for num in data:
#     print(num * 'x')

max_count = 0
max_numbers = []
while max_count != max(data):
    vertical = ''
    # print(data)
    for num in data:
        if num == max(data) - max_count or num in max_numbers:
            vertical += 'x'
            max_numbers.append(num)
        else:
            vertical += ' '   
            # data.remove(num)
    max_count += 1
    # print(data)
    print(vertical)
