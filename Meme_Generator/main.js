// Get the form and container elements from the HTML
const form = document.querySelector('.form')
const container = document.querySelector('.Container')

// Add a submit event listener to the form to handle meme generation
form.addEventListener('submit', event => {
    event.preventDefault()

    // Get input values from the form
    const urlImageInput = document.querySelector('#urlImage')
    const InputForTopText = document.querySelector('#topText')
    const inputForBottomText = document.querySelector('#bottomText')

    // Create an image element to display the meme
    const image = document.createElement('img')
    image.classList.add('meme')
    const srcImage = urlImageInput.value
    image.setAttribute('src', `${srcImage}`)

    // Create h3 elements for the top and bottom text of the meme
    let memeTop = document.createElement('h3')
    memeTop.classList.add('topt-ext')
    const topTextValue = InputForTopText.value
    memeTop.innerText = topTextValue

    const memeBottom = document.createElement('h3')
    memeBottom.classList.add('bottom-text')
    const bottomTextValue = inputForBottomText.value
    memeBottom.innerText = bottomTextValue

    // Create a button element to delete the meme
    const deleteButton = document.createElement('button')
    deleteButton.classList.add('delete')
    deleteButton.innerText = 'Delete'

    // Check if an image URL is provided
    if (srcImage) {
        // Create a div container for the meme and append the meme elements to it
        const div = document.createElement('div')
        div.classList.add('memeContainer')
        div.appendChild(memeTop)
        div.appendChild(memeBottom)
        div.appendChild(image)
        div.appendChild(deleteButton)
        container.appendChild(div)
    } else {
        // If no image URL is provided, show an alert message
        alert('Please add an URL')
    }
})

// Add a click event listener to the container to handle meme deletion and form reset
container.addEventListener('click', event => {
    const target = event.target

    // Check if the clicked element is the delete button
    if (target.className === 'delete') {
        // Remove the meme container when the delete button is clicked
        target.parentElement.remove()
    }

    // Reset the form after adding the meme or clicking the delete button
    form.reset()
})
