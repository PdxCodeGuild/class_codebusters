

function randGen() {
    let myletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()';
    let randPass = ''
    let num = prompt('Enter the length of your password: ');
    for (let i = 0; i < num; i++) {
        randPass += myletters.charAt(Math.floor(Math.random() * myletters.length));
    }
    console.log(randPass)
    return randPass
}
document.getElementById("psword").innerHTML = randGen("randPass");
