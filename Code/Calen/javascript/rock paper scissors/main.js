const rock = document.getElementById('rock')
const paper = document.getElementById('paper')
const scissors = document.getElementById('scissors')
const result = document.getElementById('result')
const winTracker = document.getElementById('win-tracker')
const lossTracker = document.getElementById('loss-tracker')
const ratioTracker = document.getElementById('ratio-tracker')


rock.addEventListener('click', () => playRPS('rock'))
paper.addEventListener('click', () => playRPS('paper'))
scissors.addEventListener('click', () => playRPS('scissors'))


function playRPS(player){
    const npc = ['rock','paper','scissors'][Math.floor(Math.random() * 3)]
    console.log(player, npc)
    let wins = parseInt(winTracker.textContent)
    let losses = parseInt(lossTracker.textContent)

    if (player == npc){
        result.textContent = 'It was a tie!'
    }
    else{
        if (player === 'rock'){
            choices = ['scissors','rock','paper']
        } 
        else if (player === 'paper'){
            choices = ['rock','paper','scissors']
        }
        else if (player === 'scissors'){
            choices = ['paper','scissors','rock']
        }

        if (choices.indexOf(player) > choices.indexOf(npc)){
            result.textContent = '${player} beats ${npc}, you win!'
            winTracker.textContent = wins + 1
        }
        else{
            result.textContent = '${npc} beats ${player}, you lose!'
            lossTracker.textContent = losses + 1
        }
    }




}
