# Credit Card Validation
# Let's write a function which returns whether a string containing a credit card number is 
# valid as a boolean. The steps are as follows:

# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.
# For example, the worked out steps would be:

# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
# 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
# 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
# 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
# 85
# 5
# Valid!

def getUserInput():
    rawUserInput = input("Please enter 16 digits: ")
    listUserInput = rawUserInput.split(' ')
    if len(listUserInput) < 16:
        return False
    for i in range(len(listUserInput)):
        listUserInput[i] = int(listUserInput[i].strip())
        if (listUserInput[i] > 9) or (listUserInput[i] < 0):
            return False
    return listUserInput

def getCheckDigit(listInput):
    checkDigit = listInput[len(listInput) - 1]
    return checkDigit

def removeCheckDigit(listInput):
    listInput.pop()
    return listInput

def reverseDigits(listInput):
    reversed = []
    i = len(listInput) - 1
    while i >= 0:
        reversed.append(listInput[i])
        i -= 1
    return reversed

def doubleEOE(listInput):
    for i in range(0, len(listInput), 2):
        listInput[i] *= 2
    return listInput

def subtractNine(listInput):
    for i in range(len(listInput)):
        if listInput[i] > 9:
            listInput[i] -= 9
    return listInput

def sumValues(listInput):
    sum = 0
    for i in listInput:
        sum += i
    return sum

def getSecondDigit(sum):
    sum
    while sum > 99:
        sum //= 10
    return sum % 10

def main():
    userInput = getUserInput()
    # print(userInput)
    checkDigit = getCheckDigit(userInput)
    # print(checkDigit)
    newList = removeCheckDigit(userInput)
    # print(newList)
    reversedList = reverseDigits(newList)
    # print(reversedList)
    doubleEONum = doubleEOE(reversedList)
    # print(doubleEONum)
    subNine = subtractNine(doubleEONum)
    # print(subNine)
    sum = sumValues(subNine)
    # print(sum)
    single = getSecondDigit(sum)
    # print(single)
    if single == checkDigit:
        return True
        # return("Your Card is Valid!")
    else:
        return False
        # return("Sorry, Your Card is Not Valid!")
print(main())

# 1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6
# 4,5,5,6,7,3,7,5,8,6,8,9,9,8,5,5