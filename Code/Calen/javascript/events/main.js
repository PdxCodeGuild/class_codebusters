let box = document.getElementById('box')
let label = document.getElementById('color-label')


box.addEventListener('mouseenter', scale)
box.addEventListener('mouseleave', scale)
box.addEventListener('click', randomcolor)


box.addEventListener('mousemove', function(event){
    let xAxis = event.screenX
    let yAxis = event.screenY
    box.textContent = `${xAxis}x, ${yAxis}Y`
})

function scale(){
    box.classList.toggle('scale-larger')
}

function randomcolor(event){
    let color = Math.floor(Math.random()*16777215).toString(16)
    console.log(color)
    box.parentElement.style.backgroundColor = `#${color}`
    label.textContent =  `#${color}`
}

label.addEventListener('click', function(){
    box.classList.toggle('hide')
})