data = []
ind = []


def peaks(nums):
    for i in range(len(nums)-1):  # itterates through list, prevents out of range
        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
            data.append('p')  # adds peak identifier to list
        else:
            data.append('')  # adds space where no peak was identified
    for i in range(len(data)-1):  # loops through list
        if data[i] == 'p':  # finds index of all p's
            ind.append(i)  # adds index to new list
    return(ind)


data2 = []
ind2 = []


def valleys(nums):
    for i in range(len(nums)-1):  # itterates through list, prevents out of range
        if nums[i] < nums[i-1] and nums[i] < nums[i+1] and nums[i] > nums[0]:
            data2.append('v')  # adds valley identifier to list
        else:
            data2.append("")  # adds space where no valley was identified
    for i in range(len(data2)-1):
        if data2[i] == 'v':
            ind2.append(i)  # adds the index of valleys to new list
    return(ind2)


ind3 = []


def peaksandvalleys(nums):  # runs both functions
    peaks(nums)
    valleys(nums)
    ind3 = ind + ind2  # combines returns from both functions to new list
    ind3 = sorted(ind3)  # sorts list so the indexes are in order
    print(ind3)


peaksandvalleys([1, 2, 3, 4, 5, 6, 7, 6, 5, 4,
                5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9])
