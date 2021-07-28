// create rps list for the computer
const rpsList = ['rock', 'paper', 'scissors'];

// function to get the computers choice
function getComp(rpsList) {
    let compChoice = rpsList[Math.floor(Math.random() * rpsList.length)];
    //console.log(compChoice); // for debugging
    return compChoice;
}

// function to get the users choice and convert it to lower case
function getChoice() {
    let userChoice = prompt("Pick rock, paper, or scissors");
    userChoice = userChoice.toLowerCase();
    //console.log(userChoice);  // for debugging
    return userChoice;
}

// function to get the results of the game and return them to the user
function rps(compChoice, userChoice) {
    //console.log(compChoice, userChoice);  // for debugging
    if (userChoice == compChoice) {
        alert('Tie')
    } else if (userChoice == 'paper' && compChoice == 'rock') {
        alert('You won, paper covers rock!')
    } else if (userChoice == 'paper' && compChoice == 'scissors') {
        alert('You lost, scissors cuts paper!')
    } else if (userChoice == 'rock' && compChoice == 'paper') {
        alert('You lost, paper covers rock!')
    } else if (userChoice == 'rock' && compChoice == 'scissors') {
        alert('You won, rock crushes scissors!')
    } else if (userChoice == 'scissors' && compChoice == 'rock') {
        alert('You lost, rock crushes scissors!')
    } else {
        alert('You won, scissors cuts paper!')
    }
}

// call the functions
let compChoice = getComp(rpsList);
let userChoice = getChoice();
rps(compChoice, userChoice);