
function rps(){
    let rps = ['rock', 'paper', 'scissors'];

    let npc = rps[Math.floor(Math.random()*3)];
    let choice = prompt('Would you like rock, paper, or scissors?');

    if (choice == 'rock'){
        rps = ['paper', 'rock', 'scissors'];
    } 
    
    else if (choice == 'paper'){
        rps = ['scissors', 'paper', 'rock'];
    } 
    
    else if (choice == 'scissors'){
        rps = ['rock', 'paper', 'scissors'];
    } 
    
    else { 
        alert("Incorrect input.");
        choice = false
    }
    
    if (choice) {
        if (rps.indexOf(choice) > rps.indexOf(npc)){
            alert('You won! NPC picked '+npc)
        }
    } 
    
    else if (choice == npc){
        alert('You Lost! NPC picked '+npc)
    }
    
    else {
        alert('You Lost! NPC picked '+npc)
    }

}

function rot(){
    const alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9',]
    let indexAdjustment = 0
    while (true){
        indexAdjustment = parseInt(prompt('Please advise on ROT number for cipher'))

        if (! isNaN(indexAdjustment)){
            break
        }
        else { 
            alert('Please select a valid number')
        }
    }

    let nonCodedText = (prompt('please insert your text')).split('')
    console.log(nonCodedText)


    for (i in nonCodedText){

        try {
            nonCodedText[i] = alph[parseInt(i)+indexAdjustment]
            
            console.log(nonCodedText[i], alph[parseInt(i)+indexAdjustment], nonCodedText)
        }
        catch(e){
            tempIndexAdjustment = (i+indexAdjustment)-(alph.length)-1
            nonCodedText[i] = alph[tempIndexAdjustment]
        }
    }

    alert('Here is your converted text ' + nonCodedText)


}

function ccv(){
    
}

let lab = prompt("Would you like to use, RPS, CCV, or ROT13?")


if (lab == 'RPS' || lab == 'rps'){
    rps()
}

if (lab == 'ROT' || lab == 'ROT13'){
    rot()
}
if (lab == 'ccv' || lab == 'CCV'){
    rot()
}

