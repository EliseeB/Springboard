$(document).ready(function() {
    $('.form').submit( function(event) {
        event.preventDefault()
        const title = $('#title').val()
        const rating = $('#rating').val()
        updateList(title, rating)
        $('#movie-title').val('')
        $('#movie-rating').val('')
    } )
})

const updateList = (title, rating) => {
    const movieItem = `<section class="movie">
    <p>Title: ${title}</p>
    <p>Ratinng: ${rating}/10</p>
    <button class="delete-btn">Delete</button>
    </section>`
    if (title.length >= 2) {
    $('.movies-list').append(movieItem)
    }
}

$('.movies-list').on('click', '.delete-btn', function() {
    $(this).parent('.movie').remove()
})