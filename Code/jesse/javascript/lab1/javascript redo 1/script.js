
//Random Password Generator

// characters to choose for password
const ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
const ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
const ascii_letters = ascii_lowercase + ascii_uppercase

const digits = '0123456789'
const punctuation = `!"#$%&'()*+,-./:;<=>?@[\\]^_\`{|}~`

const password_char = ascii_letters + digits + punctuation

// get password length from user and convert to int
const n = prompt('Enter a number for password length: ')

let password = ''

// randomly select characters from password_char until password length is reached
let count = 0
while (count < n) {
    password += password_char.charAt(Math.floor(Math.random() * password_char.length))
    count++
}

alert(password)