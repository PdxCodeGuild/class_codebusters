let addButton= document.getElementById("add");
let removeButton= document.getElementById("remove");
let addTodo=document.getElementById("todo");
let incompleteTask=document.getElementById("incomplete-tasks");
let completedTasks=document.getElementById("completed-tasks");
let list=document.getElementById("todolist");
let inputValue=""

addButton.addEventListener('click', function() {
    // let todo = addTodo.value
    // console.log(todo)
    
    let valueinput=addTodo.value
    console.log(valueinput)

    let li=document.createElement("li");
    li.classList.add('todoitem2')
    let text_todo=document.createElement('div');
    text_todo.innerHTML=valueinput

    let todolist = []
    todolist.push(valueinput)
    console.log(todolist)

    li.appendChild(text_todo)
    list.appendChild(li)

});

for (let i=0; i<addTodo.length; i++) {
    inputValue = inputValue + addTodo.[i]
}

document.getElementById("li").innerHTML = inputValue

// function removeFromList(){
//     let todolist = []


//     let removelist = document.getElementById(todoitem2)
//     removelist.removeChild(removelist.valueinput)
// }

// removeButton.addEventListener('click', function() {
//     let todolist = []
//     let valueinput=addTodo.value
//     todolist.push(valueinput)
//     console.log(todolist)
// });

