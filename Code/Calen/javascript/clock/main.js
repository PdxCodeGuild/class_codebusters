let clockData = document.getElementById('clock')

let clockSwitch = document.getElementById('clock-switch')
let countdownSwitch = document.getElementById('countdown-switch')
let stopWatchSwitch = document.getElementById('stop-watch-switch')

let stopWatchGo = document.getElementById('stopWatchGo')
let stopWatchLap = document.getElementById('stopWatchLap')
let stopWatchStop = document.getElementById('stopWatchStop')
let timerArea = document.getElementById('timer-area')

let countdownTime = document.getElementById('countdown-time')
let countdownStart = document.getElementById('countdown-start')
let countdownStop = document.getElementById('countdown-stop')

clockControl()
window.setInterval(clockControl, 1000)



stopWatchSwitch.addEventListener('click', function(){
    stopWatchSwitch.checked = true
    clockSwitch.checked = false
    countdownSwitch.checked = false
})
clockSwitch.addEventListener('click', function(){
    clockSwitch.checked = true
    stopWatchSwitch.checked = false
    countdownSwitch.checked = false
})
countdownSwitch.addEventListener('click', function(){
    countdownSwitch.checked = true
    stopWatchSwitch.checked = false
    clockSwitch.checked = false
})


function clockControl(){
    if (clockSwitch.checked){
        let date = new Date();
        clockData.textContent = `${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`
    } 
    else if (countdownSwitch.checked){

    }
    else if (stopWatchSwitch.checked){

    }

}


function stopwatchStart(){
}


countdownStart.addEventListener('click', function(){
    date = Date(minutes=countdownTime.textContent)
    console.log(date)
})
