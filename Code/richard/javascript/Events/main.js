let box = document.getElementById('box')
let label = document.getElementById('color-label')

box.addEventListener('mouseenter', function(){
    box.classList.add('scale-larger')
})

box.addEventListener('mouseleave', function(){
    box.classList.remove('scale-larger')
})

box.addEventListener('mousemove', function(event){
    let x = event.screenX
    let y = event.screenY
    box.textContent = `${x}x, ${y}y`
})

box.addEventListener('click', function(){
    const randomColor = Math.floor(Math.random() * colors.length)
    box.parentElement.style.backgroundColor = colors[randomColor]
    label.textContent = colors[randomColor]
})

label.addEventListener('click', function(){
    box.classList.toggle('hidden')
})