const rock = document.getElementById('rock')
const paper = document.getElementById('paper')
const scissors = document.getElementById('scissors')
const result = document.getElementById('result')
const winTracker = document.getElementById('win-tracker')
const lossTracker = document.getElementById('loss-tracker')
const ratioTracker = document.getElementById('ratio-tracker')

rock.addEventListener('click', function () {
  playRPS('rock')
})

paper.addEventListener('click', () => {
  playRPS('paper')
})

scissors.addEventListener('click', function(){
  playRPS('scissors')
})

function playRPS(player){
  let choices = ['rock', 'paper', 'scissors']
  const index = Math.floor(Math.random() * 3)
  const npc = choices[index]
  let wins = parseInt(winTracker.textContent)
  let losses = parseInt(lossTracker.textContent)

  if(player === npc){
    result.textContent = "It was a tie!"
  }
  else {
    if (player === 'rock'){
      choices = ['scissors', 'rock', 'paper']
    }
    else if (player === 'paper'){
      choices = ['rock', 'paper', 'scissors']
    }
    else if (player === 'scissors'){
      choices = ['paper', 'scissors', 'rock']
    }
    if(choices.indexOf(player) > choices.indexOf(npc)){
      result.textContent = `${player} beats ${npc}, you win!`

      wins++
      winTracker.textContent = wins
      ratio = (wins / (wins + losses)) * 100
      ratioTracker.textContent = `${Math.round((ratio + Number.EPSILON) * 100) / 100}%`
      ratioTracker.style.color = 'green'
    }
    else{
      result.textContent = `${npc} beats ${player}, you lose.`

      losses++
      lossTracker.textContent = losses
      ratio = (wins / (wins + losses)) * 100
      ratioTracker.textContent = `${Math.round((ratio + Number.EPSILON) * 100) / 100}%`
      ratioTracker.style.color = 'red'
    }
  }
}