const lower = 'abcdefghijklmnopqrstuvwxyz'
const upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
const digits = '1234567890'
const special = '!@#$%^&*()-=_+[]{};\':",.<>/\\`~|'


function genSegment(source, num){
  let counter = 0
  let passSegment = ''
  while(counter < num){
    passSegment += randChoice(source)
    counter++
  }
  return passSegment
}

function randChoice(string){
  let index = Math.floor(Math.random() * string.length)
  return string.charAt(index)
}

function shuffle(array){
  for(let i=0; i<array.length; i++){
    const j = Math.floor(Math.random() * array.length)
    let temp = array[i]
    array[i] = array[j]
    array[j] = temp
  }
  return array
}

function validateInt(message){
  while(true){
    const length = parseInt(prompt(message))
    if(isNaN(length)){
      alert('Invalid number, try again.')
      continue
    }
    break
  }
  return length
}

function generatePassword(){
  let numLower = validateInt('How many lowercase letters?')
  let numUpper = validateInt('How many uppercase letters?')
  let numDigits = validateInt('How many digits?')
  let numSpecial = validateInt('How many special characters?')

  let password = ''
  password += genSegment(lower, numLower)
  password += genSegment(upper, numUpper)
  password += genSegment(digits, numDigits)
  password += genSegment(special, numSpecial)

  let passArray = password.split('')
  passArray = shuffle(passArray)
  password = passArray.join('')

  alert(password)
}