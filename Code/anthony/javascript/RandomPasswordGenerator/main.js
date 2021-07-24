const string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"


function randGen(string){
  let randPass = ''
  let num = prompt('Enter your password length:')
  for(let i = 0; i<num; i++){
    let index = Math.floor(Math.random() * string.length)
    randPass += string.charAt(index)
  }
  return randPass
}

const password = randGen(string)
alert(password)