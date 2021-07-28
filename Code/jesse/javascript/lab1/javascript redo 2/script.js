
// Rot Cypher

const ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

// array of lowercase alphabet
const alphabet = ascii_lowercase.split('')

// get amount of ROT rotation from user
let rot_input = prompt('Enter amount of rotation to be used in encryption: ').toLowerCase()

rot_input = parseInt(rot_input)

// get string of letters from user, convert to lowercase and array
let user_input = prompt('Enter a series of letters: ').toLowerCase()

user_input = user_input.split('')

// encrypt the user input string of letters using ROT
let encrypted_input = []

for (letter of user_input) {
    const alpha_index = alphabet.indexOf(letter)
    const rot = rot_input
    const rotation = (alpha_index + rot) % 26
    encrypted_input.push(alphabet[rotation])
}

encrypted_input = encrypted_input.join('')

alert(encrypted_input)