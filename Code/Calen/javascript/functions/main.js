

function functionName(color){
    console.log('hello from a function')
    console.log(color)
}

functionName('blue')



function add(num1,num2){
    console.log(num1+num2)
}

let subtract = function(num1,num2) {
    console.log(num2-num1)
}


let multiply = (num1, num2) => {
    console.log(num1*num2)
}

let square = function(num){
    console.log(num*num)
}

let square2 = num => console.log(num*num)


add(1,2)
subtract(1,2)
multiply(4,5)
square(4)
square2(4)