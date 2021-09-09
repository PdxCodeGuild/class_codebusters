
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# Returns the indices of peaks. A peak has a lower number on both the left and the right.
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


#find how much water is needed
peaks_indices = peaks(data)
valleys_indices = valleys(data)
print(peaks_indices)
print(valleys_indices)

water_data = []

for x, y in zip(peaks_indices, valleys_indices):
    height = data[x] - data[y]
    half_base = y - x
    area = half_base * height
    water_data.append(area)
print(water_data)


# water = ''
# for i in range(len(data)):
#     if data[i] in peaks_indices:
#         water += '0 '
#     else:
#         water += '  '
#     print(water)

# Draws a vertical graph from numbers in "data"
max_count = 0
max_numbers = []
while max_count != max(data):
    vertical = ''
    for i in range(len(data)):
        
            if data[i] == max(data) - max_count or data[i] in max_numbers:
                vertical += 'x '
                max_numbers.append(data[i])
            #     # elif i in range(data.index(max(data)), data.index(max(data)) + 6):
            # elif data[i-1] in max_numbers:
                # vertical += '0 '
            elif i in range(p, p + 6):
                vertical += '0 '
                # for p in peaks_indices: 
            else:        
                vertical += '  '  
            
    max_count += 1
    print(vertical)
