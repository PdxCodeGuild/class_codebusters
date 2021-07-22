//-----------------------------------------------#
// PDX Code Guild
// Class CodeBusters
// Lab 01 - Javscript Redo
// Jared Nistler
//-----------------------------------------------

//-----------------------------------------------#
// Rock, Paper, Scissors
//-----------------------------------------------#

let choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"];
let win_rock = ["Lizard", "Scissors"];
let win_paper = ["Spock", "Rock"];
let win_sci = ["Lizard", "Paper"];
let win_liz = ["Spock", "Paper"];
let win_spock = ["Scissors", "Rock"];

function throwChoice(user_input, comp_input) {
  if (user_input === comp_input) {
    return "It was a tie!";
  } else if (user_input === "Rock" && win_rock.includes(comp_input)) {
    return "You win! Rock crushes scissors and lizards";
  } else if (user_input === "Paper" && win_paper.includes(comp_input)) {
    return "You win! Paper disproves spock and covers rock";
  } else if (user_input === "Scissors" && win_sci.includes(comp_input)) {
    return "You win! Scissors cuts paper and lizards";
  } else if (user_input === "Lizard" && win_liz.includes(comp_input)) {
    return "You win! Lizards eat paper and poison Spock";
  } else if (user_input == "Spock" && win_spock.includes(comp_input)) {
    return "You win! Spock vaporizes rock and smashes scissors";
  } else {
    return "You lose. Womp womp.";
  }
}

function randChoice(array) {
  let rand_int = Math.random();
  rand_int *= array.length;
  rand_int = Math.floor(rand_int);
  return array[rand_int];
}

function endMessage(user, comp, result) {
  return "You threw " + user + ". The computer threw " + comp + ". " + result;
}

function rockPaperScissors() {
  let user_choice = prompt(
    "Make your selection: Rock, Paper, Scissors, Lizard, Spockor, or Exit:"
  );

  if (choices.includes(user_choice)) {
    comp_choice = randChoice(choices);
    let result = throwChoice(user_choice, comp_choice);
    alert(endMessage(user_choice, comp_choice, result));
  }
}

//-----------------------------------------------#
// Random Password Generator
//-----------------------------------------------#

