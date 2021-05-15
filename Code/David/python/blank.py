data2 = []
ind2 = []


def valleys(nums):
    # itterates through list  # checks value of indexes on either side is greater
    for i in range(len(nums)):
        if nums[i] < nums[i-1] and nums[i] < nums[i+1] and nums[i] > nums[0]:
            data2.append('v')  # adds valley identifier to list
        else:
            data2.append("")  # adds space where no valley was identified
    for i in range(len(data2)):
        if data2[i] == 'v':
            ind2.append(i)
    print(ind2)


valleys([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9])
