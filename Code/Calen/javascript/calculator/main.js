const operators = document.querySelector('.operators')
const numbers = document.querySelector('.numbers')
const display = document.getElementById('display')
const display2 = document.getElementById('display2')

let lastOperand = 0

function back(){
    display.textContent = display.textContent.slice(0, -1)
}

function negate(){
    display.textContent = eval(display.textContent*-1)
}

function equals(){
    console.log(lastOperand)
    if (clearNext(display2)){
        doubleEquals()
    }
    else{
        lastOperand += display.textContent
    }
    let temp = display2.textContent + display.textContent + '='
    let answer = eval(display2.textContent + display.textContent)
    display2.textContent = temp
    display.textContent = answer
    console.log('running equals function')
}

function doubleEquals(){
    console.log(display)
    console.log(lastOperand)
    display.textContent += lastOperand
}

function clearNext(display2){
    if (display2.textContent.includes('=')){
        display2.textContent = ''
        return true
    } 
    return false

}

function operand(operator){
    clearNext(display2)
    lastOperand = operator
    display.textContent += operator
    display2.textContent += display.textContent
    display.textContent = ''

}

function percentinate(){
    clearNext(display2)
    display.textContent = eval(display.textContent + '/100')
}

function clear(){
    display.textContent = ''
    display2.textContent = ''
}


for (operator of operators.children){
    console.log(operator.textContent)
}

document.addEventListener('keydown', function(event){
    console.log(event.key)
    if ('1234567890.'.includes(event.key)){
        display.textContent += event.key
    }
    
    switch (event.key){

        case '=':
            equals()
            break

        case '+': 
        case '/': 
        case '*': 
        case '-':
            operand(event.key) 
            break
        
        case 'Backspace':
            back()
            break
        case 'Delete':
            clear()
            break
    }
})


for (let operator of operators.children){
    operator.addEventListener('click', function(){
        if (operator.textContent ==='⌫'){
            back()
        }
        else if (operator.textContent ==='+/-'){
            negate()
        }
        else if (operator.textContent ==='='){
            equals()
        }
        else if (operator.textContent ==='CLEAR'){
            clear()
        }
        else if (operator.textContent ==='%'){
            percentinate()
        }
        else{
            operand(operator.textContent)
        }
    })
}

for (let number of numbers.children){
    number.addEventListener('click', function(){
        display.textContent += number.textContent
    })
}
