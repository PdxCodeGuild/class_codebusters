//-----------------------------------------------#
// PDX Code Guild
// Class CodeBusters
// Lab 01-03 - Javscript Redo
// Jared Nistler
//-----------------------------------------------

//-----------------------------------------------#
// Utilities
//-----------------------------------------------#

function randChoice(obj) {
  let rand_int = Math.random();
  rand_int *= obj.length;
  rand_int = Math.floor(rand_int);
  return obj[rand_int];
}

function shufArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return(array)
}

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

const lower_bank = "abcdefghijklmnopqrstuvwxyz";
const upper_bank = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const digit_bank = "0123456789";
const symbol_bank = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c";
let pass = "";

function genPass(char_source, num) {
  let counter = 0;
  pass_seg = "";
  while (counter < num) {
    pass_seg += randChoice(char_source);
    counter++;
  }
  return pass_seg;
}

function randPassGen() {
  let num_upper = prompt("How many upper-case letters?");
  let num_lower = prompt("How many lower-case letters?");
  let num_digit = prompt("How many digits?");
  let num_sym = prompt("How many symbols?");

  pass =
    genPass(upper_bank, num_upper) +
    genPass(lower_bank, num_lower) +
    genPass(digit_bank, num_digit) +
    genPass(symbol_bank, num_sym);
  console.log(pass)
  let passList = pass.split("");
  pass = shufArray(passList);
  let pass_final = pass.join('')
  alert("Your password is: " + pass_final)
}

//-----------------------------------------------#
// Rot13
//-----------------------------------------------#


function encryptStr(text, num) {
  let encrypted = "" 
  for (char of text) {
    encrypted += lower_bank[((lower_bank.indexOf(char)) + num) % 26]
  }
  return encrypted
}

function decryptStr(text, num) {
  let decrypted = "" 
  for (char of text) {
    decrypted += lower_bank[((lower_bank.indexOf(char)) - num) % 26]
  }
  return decrypted
}

function rotCypher(str) {
  let user_text = document.getElementById("RotTextArea").textContent
  let rot_num = document.getElementById("RotNumArea").textContent;

  console.log(user_text)
  console.log(rot_num)

  // if (str == "e"){
  //   encryptStr()
  // }
  // else {
  //   decryptStr()
  // }

}