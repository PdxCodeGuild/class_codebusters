const todoItems = document.getElementById('todo-items')
const addInput = document.getElementById('add-input')
const addSelect = document.getElementById('add-select')
const addBtn = document.getElementById('add-btn')


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
  const ul = document.createElement('ul')
  todoItems.appendChild(ul)
  for(let todo of todos.todos){
    const li = document.createElement('li')
    li.className = todo.priority
    li.textContent = todo.text
    if(todo.completed_date){
      li.className = 'completed'
    }
    ul.appendChild(li)
  }
}

addBtn.addEventListener('click', () => {
  const todoItem = addInput.value
  const todoPriority = addSelect.value
  const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0]


  fetch('http://localhost:8000/create/', {
    method: "POST",
    body: {
      todoItem: todoItem,
      todoPriority: todoPriority
    },
    headers: {'X-CSRFToken': csrfToken.value}
  })
})


getTodos()