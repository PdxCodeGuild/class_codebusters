const newTodo = document.getElementById('new-todo')
const addTodo = document.getElementById('add-todo')
const listItems = document.getElementById('list-items')
const listComplete = document.getElementById('list-complete')

// TODO, move items around
const todoItems = []
const completeItems = []

function displayTodoItems(){
  for(let item of todoItems){
    const divItem = document.createElement('div')
    divItem.setAttribute('class', 'item')
    const p = document.createElement('p')
    p.textContent = item
    const div = document.createElement('div')
    const btnComplete = document.createElement('button')
    btnComplete.textContent = 'Complete'
    btnComplete.addEventListener('click', function() {
      completeTodo(btnComplete, todoItems, completeItems)
    })
    const btnRemove = document.createElement('button')
    btnRemove.textContent = 'Delete'
    btnRemove.addEventListener('click', function(){
      removeTodo(btnRemove, todoItems)
    })

    divItem.append(p)
    divItem.append(div)
    div.append(btnComplete)
    div.append(btnRemove)
    listItems.append(divItem)
  }
}

function displayCompletedItems(){
  for(let item of completeItems){
    const divItem = document.createElement('div')
    divItem.setAttribute('class', 'item')
    const p = document.createElement('p')
    p.textContent = item
    const div = document.createElement('div')
    const btnUndo = document.createElement('button')
    btnUndo.textContent = 'Undo'
    btnUndo.addEventListener('click', function() {
      completeTodo(btnUndo, completeItems, todoItems)
    })
    const btnRemove = document.createElement('button')
    btnRemove.textContent = 'Delete'
    btnRemove.addEventListener('click', function(){
      removeTodo(btnRemove, completeItems)
    })


    divItem.append(p)
    divItem.append(div)
    div.append(btnUndo)
    div.append(btnRemove)
    listComplete.append(divItem)
  }
}

function clearTaskList(list){
  while(list.firstChild){
    list.removeChild(list.firstChild)
  }
}

function completeTodo(btn, arrayFrom, arrayTo){
  const item = btn.parentElement.parentElement
  const index = arrayFrom.indexOf(item.firstChild.textContent)
  const [complete] = arrayFrom.splice(index, 1)
  arrayTo.push(complete)

  clearTaskList(listItems)
  clearTaskList(listComplete)
  displayTodoItems()
  displayCompletedItems()
}

function removeTodo(btn, array){
  const item = btn.parentElement.parentElement
  const index = array.indexOf(item.firstChild.textContent)
  array.splice(index, 1)

  clearTaskList(listItems)
  clearTaskList(listComplete)
  displayTodoItems()
  displayCompletedItems()
}


addTodo.addEventListener('click', function () {
  todoItems.push(newTodo.value)
  newTodo.value = ''
  clearTaskList(listItems)
  displayTodoItems()
})