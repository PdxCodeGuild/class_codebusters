const readline = require("readline");
let pass_length = 5


const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });




elements = ['A','B','C', 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']

let password = ""
let num = 62
let i = 0
rl.question("What should be the password length? ", function (answer) {
    pass_length = parseInt(answer)
    while(i < pass_length){
        character = ""
        
        idx = Math.floor((Math.random() * num) );
        if ( idx > 35){
            idx = idx - 36
            character = elements[idx].toLowerCase()
        }else{
            character = elements[idx]
        }
        password += character
        i += 1
        
    }
    
    console.log(password)
    rl.close()
  });