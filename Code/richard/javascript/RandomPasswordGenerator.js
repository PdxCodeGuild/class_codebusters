// # Random Password Generator
// # Part 1
// # Let's generate a password of length n using a while loop and random.choice, this will be a string 
// # of random characters, e.g. a62xB95. Allow the user to enter the value of n, remember to convert its 
// # type to an int, as input returns a string. Hint: random.choice can be used to pick a character out 
// # of a string, as well as an element out of a list.
// import random
// import string


// allChar = String.fromCharCode(97-122) + String.fromCharCode(65-90) + String.fromCharCode(48-57) + String.fromCharCode(33-47)
let allChar=""

for (let i = 97; i <= 122; i++){
    allChar += String.fromCharCode(i)
}
for (let i = 65; i <= 90; i++){
    allChar += String.fromCharCode(i)
}
for (let i = 33; i <= 57; i++){
    allChar += String.fromCharCode(i)
}

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
function generatePassword(n){
    let password = ''
    for (let i = 0; i < n; i++){
        password += allChar[getRandomInt(0,allChar.length)]
    }
    return password
}
        

userInput = parseInt(prompt("Please enter the length of password: "))


alert(generatePassword(userInput))

// # Part 2 (optional)
// # Ask the user for how many lowercase letters, uppercase letters, numbers, and special characters 
// # they'd like in their password. You do not want the pieces in order (e.g. 3 lowercase letters followed 
// # by 3 uppercase letters...). You can use list(password_string) or password_string.split('') to convert 
// # the string to a list, random.shuffle(password_list) to shuffle it, and then ''.join(password_list) to 
// # turn it back into a string.


// low = string.ascii_lowercase
// ups = string.ascii_uppercase
// dig = string.digits
// special = string.punctuation

// def generatePassword(l,u,s,d):
//     password_list = []
//     for i in range(l):
//         password_list += random.choice(low)
//     for i in range(u):
//         password_list += random.choice(ups)
//     for i in range(d):
//         password_list += random.choice(dig)
//     for i in range(s):
//         password_list += random.choice(special)
//     random.shuffle(password_list)
//     return ''.join(password_list)


// lowers = int(input("Please enter how many lowercase characters in password: "))
// uppers = int(input("Please enter how many uppercase characters in password: "))
// digs = int(input("Please enter how many digits in password: "))
// specials = int(input("Please enter how many special characters in password: "))
// print(generatePassword(lowers,uppers,specials,digs))
