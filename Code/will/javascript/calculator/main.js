let output=document.querySelector("#output")
let display=document.querySelector("#display")
let enter=document.getElementById("enter")
let calc=document.getElementById("calc")
let answer=""

calc.addEventListener('click',function(){
    output.innerText = eval(enter.value)
    let temp=""
    
    for(let i=0; i<enter.value.length; i++){
        
        if(enter.value[i] === '/'){
            
            temp+= '÷'
        }
        else if(enter.value[i] === '*'){
            temp += '×'
        }
        else{
            
            temp+=enter.value[i]
        }
    }
    
    display.innerText=temp
    answer=enter.value
})


function groupvalue(input){
    let temp = input
    if(input === '/'){
        temp = '÷'
    }
    else if(input === '*'){
        temp = '×'
    }
    let end = ""
    if(display.innerText[display.innerText.length-1]==="="){
        answer=output.innerText
        if(input==="="){
            let j=0
            for(let i=0;i<display.innerText.length-1;i++){
                if(display.innerText[i]==="+"||display.innerText[i]==="-"||display.innerText[i]==="÷"||display.innerText[i]==="×"){
                    j=i
                }
            }
            while(j<display.innerText.length-1){
                if(display.innerText[j] === '÷'){
                    end+= '/'
                }
                else if(display.innerText[j] === '×'){
                    end+='*'
                }
                else{
                    end+=display.innerText[j]
                }
                j++
            }
        }
        console.log(end)
        answer+=end 
        displayTemp=display.innerText
        display.innerText=""
        for(let i=0; i<displayTemp.length-1;i++){
            display.innerText+=displayTemp[i]
        }
    }
    display.innerText += temp
    if(input==="="){
        answer=eval(answer)  
    }
    else if(input==="%"){
        answer/=100
    }
    else if(input==="swap"){
        answer*= -1
    }
    else if(input==="ac"){
        answer= ""
        display.innerText=""
    }
    else if(input==="delete"){
        Answer = answer 
        answer = ""
        for(let i= 0; i<Answer.length-1;i++){
            answer+= Answer[i]
        }
    }
    else{
        answer +=input
    }
    output.innerText =answer
}

