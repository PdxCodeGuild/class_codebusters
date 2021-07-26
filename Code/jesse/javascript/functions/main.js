

function functionName(color){
    console.log("hello from a function!")
    console.log(color)
}

// functionName("blue", 12)

// add(1, 2)

function add(num1, num2){
    console.log(num1 + num2)
}

let subtract = function(num1, num2){
    console.log(num2 - num1)
}

// subtract(3, 8)

let multiply = (num1, num2) => {
    console.log(num1 * num2)
}

// multiply(2, 4)


let square = function(num) {
    console.log(num * num)
}

// square(4)

let square2 = num => console.log(num * num)

// square2(3)

let divide = function(num1, num2) {
    console.log(num1 / num2)
}

divide(num2=8, num1=4)

let hello = () => {
    console.log('hello')
}