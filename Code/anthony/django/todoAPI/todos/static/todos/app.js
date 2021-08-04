const todoItems = document.getElementById('todo-items')
const addInput = document.getElementById('add-input')
const addSelect = document.getElementById('add-select')
const addBtn = document.getElementById('add-btn')
const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0]

function getTodos(){
  fetch('http://localhost:8000/todos/')
  .then(data => data.json())
  .then(todos => renderTodos(todos))
  // .then(function(data){
  //   data.json()
  //   .then(function(todos){
  //     renderTodos(todos)
  //   })
  // })
}

function renderTodos(todos){
  // while(todoItems.firstChild){
  //   todoItems.removeChild(todoItems.firstChild)
  // }
  todoItems.textContent = ""
  const ul = document.createElement('ul')
  todoItems.appendChild(ul)
  for(let todo of todos.todos){
    const li = document.createElement('li')
    li.className = todo.priority
    li.textContent = todo.text
    li.id = todo.id
    if(todo.completed_date){
      li.className = 'completed'
    }
    li.addEventListener('click', (event) => {
      if(event.shiftKey){
        deleteTodo(li.id)
      }
      else {
        completeTodo(li.id)
      }
    })
    ul.appendChild(li)
  }
}

function deleteTodo(todoId){
  fetch('http://localhost:8000/delete/', {
    method: "POST",
    headers: {
      'X-CSRFToken': csrfToken.value
    },
    body: JSON.stringify({
      todoId: todoId
    })
  })
  .then(() => {
    getTodos()
  })
}

function completeTodo(todoId){
  console.log(todoId)
  fetch('http://localhost:8000/update/', {
    method: "POST",
    headers: {
      'X-CSRFToken': csrfToken.value
    },
    body: JSON.stringify({
      todoId: todoId
    })
  })
  .then(() => {
    getTodos()
  })
}

addBtn.addEventListener('click', () => {
  const todoItem = addInput.value
  addInput.value = ""
  const todoPriority = addSelect.value

  const data = {              // JS object
    todoItem: todoItem,
    todoPriority: todoPriority
  }

  fetch('http://localhost:8000/create/', {
    method: "POST",
    body: JSON.stringify({              // JS object
      todoItem: todoItem,
      todoPriority: todoPriority
    }),  // json string -> '{"key": "value"}'
    headers: {'X-CSRFToken': csrfToken.value}
  }) // Fetch converts body json sting to byte string -> b'100101010'
  .then(() => {
    console.log('fetching todos')
    getTodos()
  })
})


getTodos()
