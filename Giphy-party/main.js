
//  References to the necessary elements
const form = document.querySelector('.form')
const searchInput = document.getElementById('searchInput')
const searchBtn = document.querySelector('.searchBtn')
const deleteBtn = document.querySelector('.deleteBtn')
const container = document.querySelector('.imageContainer')


//  Fetch a random GIF from the Giphy API
async function getRandomGiphyData() {
    const key = 'OR4LB9eZ5Afxz6BXjKUKoqsVVVvyHgwd'
    const searchTerm = searchInput.value
    const url = `https://api.giphy.com/v1/gifs/search?q=${searchTerm}&api_key=${key}`
    const res = await axios.get(url)
    const data = res.data.data
    const randomIndex = Math.floor(Math.random() * data.length)
    return data[randomIndex]
}

//  Creates and append a GIF to the container
const createAndAppendGiphy = async () => {
    
        const results = await getRandomGiphyData()  

        const div = document.createElement('div')
        const image = document.createElement('img')
        image.src = results.images.downsized_large.url
        image.alt =  results.title

        div.appendChild(image)
        container.appendChild(div)
    

}

// Handles click events on the buttons
function handleClick(event) {

    event.preventDefault()
    const target = event.target

    if (target.classList.contains('searchBtn')) {

       createAndAppendGiphy()
       searchInput.value = ''

    } else if( target.classList.contains('deleteBtn')) {

        container.innerHTML = ''
    }
}


form.addEventListener('click', handleClick)