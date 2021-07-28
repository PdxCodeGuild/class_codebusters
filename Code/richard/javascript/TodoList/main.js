let todoList = document.querySelector('#todoList')
let completed = document.querySelector('#completed')

let todoListArr = {}
let completedArr = {}

let submitItem = document.getElementById('submitItem')
submitItem.addEventListener('click', function(){
    let addItem = document.getElementById('addItem')
    todoListArr[addItem.value] = addItem.value
    todoList.innerHTML = ""
    completed.innerHTML =""
    for(i in todoListArr){
        todoList.innerHTML += `<p>${todoListArr[i]}<button class=" m-1 btn btn-primary" id="${todoListArr[i]}" value="${todoListArr[i]}">Delete</button></p>`
    }
    for(i in completedArr){
        completed.innerHTML += `<p>${completedArr[i]}</p>`
    }
    let remove = document.getElementById(`${todoListArr[i]}`)
    remove.addEventListener('click', function(){
        completedArr[remove.value] = remove.value;
        delete todoListArr[remove.value];
        todoList.innerHTML = ""
        completed.innerHTML =""
        for(i in todoListArr){
            todoList.innerHTML += `<p>${todoListArr[i]}<button id="asdf" ">Delete</button></p>`
        }
        for(i in completedArr){
            completed.innerHTML += `<p>${completedArr[i]}</p>`
        }
    
    })
})
