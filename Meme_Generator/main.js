
const form = document.querySelector('.form')

const container = document.querySelector('.Container')



form.addEventListener('submit', event => {
    event.preventDefault()
    const urlImageInput = document.querySelector('#urlImage')

    const InputForTopText = document.querySelector('#topText')

    const inputForBottomText = document.querySelector('#bottomText')

    const image = document.createElement('img')
    image.classList.add('meme')
    const srcImage = urlImageInput.value
    image.setAttribute('src', `${srcImage}`)


    let  memeTop = document.createElement('h3')
        memeTop.classList.add('topt-ext')


    const topTextValue = InputForTopText.value
    memeTop.innerText = topTextValue
    
    const memeBottom = document.createElement('h3')
    memeBottom.classList.add('bottom-text')
    const bottomTextValue = inputForBottomText.value
    memeBottom.innerText = bottomTextValue

    const deleteButton = document.createElement('button')
    deleteButton.classList.add('delete')
    deleteButton.innerText = 'Delete'


    if (srcImage) {
        const div = document.createElement('div')
        div.classList.add('memeContainer')
        div.appendChild(memeTop)
        div.appendChild(memeBottom)
        div.appendChild(image)
        div.appendChild(deleteButton)
        container.appendChild(div)
       
    } else {
        alert('Please add an Url')
    }
})

container.addEventListener('click', event => {
    const target = event.target

    if(target.className === 'delete') {
        target.parentElement.remove()
    }
    
    form.reset()

})