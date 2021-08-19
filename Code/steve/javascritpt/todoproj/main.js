// create my lists
let taskList = []
let completeTaskList = []

// create DOM connections
const addTask = document.getElementById('add-task')
const submitTask = document.getElementById('submit-task')
const myTasks = document.getElementById('my-tasks')
const completeTask = document.getElementById('complete-task')
const completeSubmit = document.getElementById('complete-submit')
const taskDone = document.getElementById('task-done')
const deleteTask = document.getElementById('delete-task')
const deleteComplete = document.getElementById('delete-complete')


// input box with 'Enter' to add task to list
addTask.addEventListener('keypress', (event) => {
    if (event.key === 'Enter'){
        taskList.push(addTask.value)
        addTask.value = ''
        clearTaskList(myTasks)
        toDoTasks(taskList)
}
})

// submit button to enter task
submitTask.addEventListener('click', () => {
    taskList.push(addTask.value)
    addTask.value = ''
    clearTaskList(myTasks)
    toDoTasks(taskList)  
})

deleteTask.addEventListener('click', () => {
    let index = taskList.indexOf(addTask.value)
    addTask.value = ''
    if (index != -1){
        taskList.splice(index, 1)
        clearTaskList(myTasks)
        toDoTasks(taskList)
}})

// create list element and add task to html
const toDoTasks = (taskList) => {taskList.forEach(function(task) {   
const li = document.createElement('li')
    li.textContent = task
    myTasks.append(li)
})
}

// clear task list - used to prevent continous add
// [run] [run, run, jump] [run, run, run, jump, jump, swim]
const clearTaskList = (list) => {
    while (list.firstChild){
        list.removeChild(list.firstChild)
    }
}

// identify and remove completed task from taskList
const moveTask = (completeTask, taskList) => {
    let index = taskList.indexOf(completeTask.value)
    if (index != -1){
        taskList.splice(index, 1)
        clearTaskList(myTasks)
        toDoTasks(taskList)
        
    }
}

// input box with 'Enter' to add task to list
completeTask.addEventListener('keypress', (event) => {
    if (event.key === 'Enter'){
        moveTask(completeTask, taskList)
        completeTaskList.push(completeTask.value)
        completeTask.value = ''
        clearTaskList(taskDone)
        completedTasks(completeTaskList)
    }
})

// button to submit completed task
completeSubmit.addEventListener('click', () => {
    moveTask(completeSubmit, taskList)
    completeTaskList.push(completeTask.value)
    completeTask.value = '' 
    clearTaskList(taskDone)
    completedTasks(completeTaskList)
})

deleteComplete.addEventListener('click', () => {
    let index = completeTaskList.indexOf(completeTask.value)
    completeTask.value = ''
    if (index != -1){
        completeTaskList.splice(index, 1)
        clearTaskList(taskDone)
        completedTasks(completeTaskList)
}})

// create list element and add task to html
const completedTasks = (completeTaskList) => {completeTaskList.forEach(function(task) {   
    const li = document.createElement('li')
        li.textContent = task
        taskDone.append(li)
    })
}

