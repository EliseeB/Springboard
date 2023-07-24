/*
JS Todos Exercise

Part 1

For this assignment you will be combining your knowledge of DOM access and events to build a todo app!

As a user, you should be able to:

    Add a new todo (by submitting a form)
    Mark a todo as completed (cross out the text of the todo)
    Remove a todo
*/


//Selectors

const body = document.querySelector('body')

const toggleDarkModeBtn = document.querySelector('.darkModeBtn')

const form = document.querySelector('form')

const formInput = document.querySelector('input[type="text"]')

const addNewTaskBtn = document.querySelector('.addNewTaskBtn')

const orderedList = document.querySelector('.taskList')




//Toggle dark mode on click

toggleDarkModeBtn.addEventListener('click', () => {
    body.classList.toggle('darkMode')
})


//Appends a new li on ol once the form submitted

form.addEventListener('submit', event => {

    event.preventDefault()

    const inputValue = formInput.value

    const newTask = document.createElement('li')

    newTask.classList.add('task')

    newTask.innerText = inputValue

    const completedTaskBtn = document.createElement('button')

    completedTaskBtn.classList.add('completedTask')

    completedTaskBtn.innerText = 'Completed'

    const deleteBtn = document.createElement('button')

    deleteBtn.classList.add('delete')

    deleteBtn.innerText = 'Delete'

    newTask.appendChild(completedTaskBtn)

    newTask.appendChild(deleteBtn)


    if (inputValue) {
        orderedList.appendChild(newTask)

    } else {
        alert('Input field must contain some text/number before adding it to your list.')
    }

    //saves updated list to localStorage
    saveTasksToLocalStorage()

    form.reset()
})


// completed and delete button


orderedList.addEventListener('click', event => {

    const target = event.target

    if (target.className === 'completedTask') {
        target.parentElement.classList.add('done')
    } else if (target.className === 'delete') {
        target.parentElement.remove()
    }

    //saves updated list to localStorage
    saveTasksToLocalStorage()
})


/*
Part 2

Now that you have a functioning todo app, save your todos in localStorage! Make sure that when the page refreshes, the todos on the page remain there.
*/


// Function to save the tasks to localStorage

const saveTasksToLocalStorage = () => localStorage.setItem('todoList', orderedList.innerHTML)


// Load tasks from localStorage on page load

document.addEventListener('DOMContentLoaded', () => {
    const savedList = localStorage.getItem('todoList')

    const darkMode = localStorage.getItem('darkMode')

    if (savedList) {
        orderedList.innerHTML = savedList
    }
})


