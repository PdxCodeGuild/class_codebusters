// # Credit Card Validation
// # Let's write a function which returns whether a string containing a credit card number is 
// # valid as a boolean. The steps are as follows:

// # Convert the input string into a list of ints
// # Slice off the last digit. That is the check digit.
// # Reverse the digits.
// # Double every other element in the reversed list.
// # Subtract nine from numbers over nine.
// # Sum all values.
// # Take the second digit of that sum.
// # If that matches the check digit, the whole card number is valid.
// # For example, the worked out steps would be:

// # 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
// # 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
// # 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
// # 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
// # 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
// # 85
// # 5
// # Valid!

function getUserInput(){
    let rawUserInput = prompt("Please enter 16 digits: ")
    let listUserInput = rawUserInput.split(',')
    if (listUserInput.length < 16){
        return False
    }
    for(let i = 0; i < listUserInput.length; i++){
        listUserInput[i] = parseInt(listUserInput[i])
        if ((listUserInput[i] > 9) || (listUserInput[i] < 0)){
            return False
        }
    }
    return listUserInput
}
function getCheckDigit(listInput){
    let checkDigit = listInput[listInput.length - 1]
    return checkDigit
}

function removeCheckDigit(listInput){
    listInput.pop()
    return listInput
}

function reverseDigits(listInput){
    let reversed = []
    let i = listInput.length - 1
    while (i >= 0){    
        reversed.push(listInput[i])
        i--
    }
    return reversed
}

function doubleEOE(listInput){
    for(let i = 0; i < listInput.length; i += 2){
        listInput[i] *= 2
    }
    return listInput
}

function subtractNine(listInput){
    for(let i = 0; i < listInput.length; i++){
        if (listInput[i] > 9){
            listInput[i] -= 9
        }
    }
    return listInput
}

function sumValues(listInput){
    sum = 0
    for(let i = 0; i < listInput.length; i++){
        sum += listInput[i]
    }
    return sum
}

function getSecondDigit(sum){
    sum
    while(sum > 99){
        sum = Math.floor(sum / 10)
    }
    return sum %= 10
}

function main(){
    let userInput = getUserInput()
    // # print(userInput)
    let checkDigit = getCheckDigit(userInput)
    // # print(checkDigit)
    let newList = removeCheckDigit(userInput)
    // # print(newList)
    let reversedList = reverseDigits(newList)
    // # print(reversedList)
    let doubleEONum = doubleEOE(reversedList)
    // # print(doubleEONum)
    let subNine = subtractNine(doubleEONum)
    // # print(subNine)
    let sum = sumValues(subNine)
    // # print(sum)
    let single = getSecondDigit(sum)
    // # print(single)
    if(single == checkDigit){
        // return True
        return("Your Card is Valid!")
    }
    else{
        // return False
        return("Sorry, Your Card is Not Valid!")
    }
}

alert(main())

// # 1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6
// # 4,5,5,6,7,3,7,5,8,6,8,9,9,8,5,5