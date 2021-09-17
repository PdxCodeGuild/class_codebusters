const rock = document.getElementById('rock')
const paper = document.getElementById('paper')
const scissors = document.getElementById('scissors')

rock.addEventListener('click', function () { 
    playRPS('rock')
})

paper.addEventListener('click', function () { 
    playRPS('paper')
})

scissors.addEventListener('click', function () { 
    playRPS('scissors')
})

function playRPS(player){
    let choices = ['rock', 'paper', 'scissors']
    const index = Math.floor(Math.random() * 3 )
    const npc = choices[index]

    if(player === npc){
    result.textContent = "It was a tie"
    }
    else {
        if(player === 'rock'){
            choices = ['scissors', 'rock', 'paper']
        }

        if(player === 'rock'){
            choices = ['rock', 'paper', 'scissors']
        }

        if(player === 'rock'){
            choices = [ 'paper', 'scissors', 'rock']
        }

        if(choices.indexOf(player) > choices.indexOf(npc))
        {
            result.textContent = `${player} beats ${npc}, you win!`
        }

        else{
            result.textContent = `${npc} beats ${player}, you lose. `
        }
    }
}