// Get the container element from the HTML with the class 'container'
const container = document.querySelector('.container');

// Define an array of colors to be used for the game
const colors = ['red', 'yellow', 'dodgerblue', 'orangered', 'green', 'purple', 'teal', 'cyan', 'blue', 'pink','red', 'yellow', 'dodgerblue', 'orangered', 'green', 'purple', 'teal', 'cyan', 'blue', 'pink'];

// Function to shuffle the array using the Fisher-Yates algorithm
const shuffle = array => {
    for (let currentIndex = array.length - 1; currentIndex > 0; currentIndex--) {
        const randomIndex = Math.floor(Math.random() * currentIndex);

        // Swap elements between currentIndex and randomIndex
        const tempIndex = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = tempIndex;
    }

    return array;
}

// Function to create the game board with shuffled cards
const createGame = () => {
    // Shuffle the colors array
    const shuffleColors = shuffle(colors);

    // Loop through the shuffled colors and create cards with corresponding colors
    for (const color of shuffleColors) {
        const card = document.createElement('div');
        card.classList.add( color);
        container.appendChild(card);
    }
}

// Variables to keep track of the first and second clicked cards, and a flag to prevent clicking on more than two cards at once
let firstCard = null;
let secondCard = null;
let checkingCards = false;

// Event listener on the container to handle card clicks
container.addEventListener('click', event => {
    // Get the clicked card element
    const clickedCard = event.target;

    // If checkingCards is true, return and prevent further clicks until the cards are checked for a match
    if (checkingCards) {
        return;
    }

    // If the clicked card is not already matched and not the same as the first clicked card
    if (!clickedCard.classList.contains('matched') && clickedCard !== firstCard) {
        if (firstCard === null) {
            // First click, reveal the card by changing its background color to the corresponding class name
            firstCard = clickedCard;
            clickedCard.style.backgroundColor = clickedCard.className;
        } else {
            // Second click, reveal the card by changing its background color to the corresponding class name
            secondCard = clickedCard;
            secondCard.style.backgroundColor = clickedCard.className;
            checkingCards = true;

            if (firstCard.className === secondCard.className) {
                // The two cards match, mark them as matched by adding a 'matched' class, reset the first and second cards, and reset the checkingCards flag
                firstCard.classList.add('matched');
                secondCard.classList.add('matched');
                firstCard = null;
                secondCard = null;
                checkingCards = false;

                // Check if all cards are matched, if yes, display a message and reset the game
                const allCards = container.querySelectorAll('.card');
                const matchedCards = container.querySelectorAll('.matched');
                if (allCards.length === matchedCards.length) {
                    alert('Congratulations! You won the game!');
                    // Reset the game by clearing the container and calling the createGame function again
                    container.innerHTML = '';
                    createGame();
                }
            } else {
                // The two cards do not match, hide the cards after a short delay by resetting their background color, reset the first and second cards, and reset the checkingCards flag
                setTimeout(() => {
                    firstCard.style.backgroundColor = '';
                    secondCard.style.backgroundColor = '';
                    firstCard = null;
                    secondCard = null;
                    checkingCards = false;
                }, 1000);
            }
        }
    }
});

// Call the createGame function to initialize the game board with shuffled cards
createGame();


