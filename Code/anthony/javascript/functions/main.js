
// def function_name():
function functionName(color, num){
  console.log("hello from a function!")
  console.log(color, num)
}

// functionName("blue", 12)


// Declaration
function add(num1, num2){
  console.log(num1 + num2)
}

// add(1, 2)

// Assigning a unnamed function to variable
let subtract = function(num1, num2){
  console.log(num2 - num1)
}

// subtract(3, 8)

// Arrow function
// let multiply = (num1, num2) => {
//   console.log(num1 * num2)
// }

// multiply(2, 4)


let square = function(num) {
  console.log(num * num)
}

// square(4)

let square2 = num => console.log(num * num)

// square2(3)

let multiply = (num1=1, num2=1) => {
  console.log(num1 * num2)
}

// multiply(num2=4, num1=2)

let divide = function(num1=1, num2=1){
  console.log(num1 / num2)
}

divide(8, 4)


let hello = () => {
  console.log('hello')
}