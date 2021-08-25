inquirer = require("inquirer")

class RockPaperScissor{
    constructor(){
        this.prompt = inquirer.createPromptModule();
        this.moves = ["rock", "paper","scissors"];
    }

    async newGame() {
        let answer = await this.prompt({
            type: 'confirm',
            name: 'new_game',
            message: "New game?"
        });
        if(answer.new_game !==true){
            console.log("bye!")
            process.exit();
        }
        this.chooseGameOption();
    }

    async chooseGameOption(){
        let answer = await this.prompt({
            type: 'list',
            name: 'game_option',
            message: "Please choose one.",
            choices: [
            {name:'Player vs Computer',value:"player_vs_computer"}, 
            {name: 'Computer vs Computer', value:"computer_vs_computer"}
            ]
        });
        this.compete(answer.game_option);
    }

    async compete(gameOption){
        let player1Label = '';
        let player1Move = '';
        let result = '';
        let computerMove = this.randomMove();
        if (gameOption === "player_vs_computer"){
            player1Move = await this.getUserMove();
            player1Label ='You';
        } else if (gameOption === "computer_vs_computer") {
            player1Move = this.randomMove();
            player1Label = 'Computer 1';
        } 
        if(player1Move==='') {
            console.log("Something went wrong. Please try again.");
            process.exit();
        }
        
        let winner = await this.getWinner(player1Move, computerMove, player1Label)

        this.printResult(winner, player1Label, player1Move,computerMove);
        this.newGame();
    }

    getWinner(player1Move, computerMove, player1Label){
        let winner = "";
        if (player1Move === computerMove) {
            winner = "no one";
        } else if (player1Move === 'rock') {
            if (computerMove === 'paper') {
                winner = "computer"
            } else {
                winner = `${player1Label}`;
            }
        } else if (player1Move === 'paper') {
            if (computerMove === 'scissors') {
                winner = "computer"
            } else {
                winner = `${player1Label}`;
            }
        } else if (player1Move === 'scissors') {
            if (computerMove === 'rock') {
                winner = "computer"
            } else {
                winner = `${player1Label}`;
            }
        } else {
            console.log("Something went wrong. Please try again.");
            process.exit();
        }

        return new Promise((resolve, reject) => {
            resolve(winner);
        }); 
    }

    printResult(winner, player1Label, player1Move,computerMove){
        console.log(`Winner: ${winner}. ${player1Label}(${player1Move}) vs Computer(${computerMove})`);
    }

    randomMove(){
        return this.moves[Math.floor(Math.random() * this.moves.length)];
    }

    async getUserMove(gameOption) {
        let answer = await this.prompt({
            type: 'list',
            name: 'move',
            message: "Choose your move.",
            choices: [
            { name: 'Rock', value: "rock" },
            { name: 'Paper', value: "paper" },
            { name: 'Scissors', value: "scissors" }
            ]
        });
        return new Promise((resolve, reject) => {
            resolve(answer.move);
        }); 
    }
}

const game = new RockPaperScissor()
game.newGame();