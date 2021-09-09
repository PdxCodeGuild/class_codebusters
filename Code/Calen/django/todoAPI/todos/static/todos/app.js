const todoItems = document.getElementById('todo-items')
const addInput = document.getElementById('add-input')
const addSelect = document.getElementById('add-select')
const addBtn = document.getElementById('add-btn')

const csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0]


function getTodos(){
    fetch('http://localhost:8000/todos/')
    .then(data => data.json())
    .then(data => renderTodos(data))
}


function renderTodos(todos){

    while(todoItems.firstChild){
        todoItems.removeChild(todoItems.firstChild)
        addInput.value =''
    }

    const ul = document.createElement('ul')
    todoItems.appendChild(ul)
    for(let todo of todos.todos){
        const li = document.createElement('li')
        li.className = todo.priority
        li.textContent = todo.text
        li.id = todo.id
        if(todo.completed_date){li.className = 'completed'}
        li.addEventListener('click', (event) => {
            if(event.shiftKey){
                deleteTodo(li.id)
            }
            else{
                completeTodo(li.id)
            }
        })
        ul.appendChild(li)
    }

}

function completeTodo(todoID){
    fetch('http://localhost:8000/update/', {
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken.value},
        body: JSON.stringify({todoID: todoID}),
    })
    .then(() => {
        getTodos()
    })
}


function deleteTodo(todoId){
    fetch('http://localhost:8000/delete/', {
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken.value},
        body: JSON.stringify({todoID: todoId}),
    })
    .then(() => {
        getTodos()
    })
}


addBtn.addEventListener('click', () => {
    const todoItem = addInput.value
    const todoPriority = addSelect.value
    
    fetch('http://localhost:8000/create/', {
        method: 'POST',
        body: JSON.stringify({
            todoItem: todoItem,
            todoPriority: todoPriority,
        }),
        headers: {'X-CSRFToken': csrftoken.value},
    })
    .then(() => getTodos())
})



getTodos()