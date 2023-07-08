/*
Write a function called countdown that accepts a number as a parameter and every 1000 milliseconds decrements the value and console.logs it. Once the value is 0 it should log “DONE!” and stop.
*/

const countdown = num => {

    //Subtracts 1 from num every 1 second as long as num is greater then 0.

    const intervalId = setInterval(function () {

        if (num > 0) {

            console.log(num--)

        } else {
            //Logs "DONE!" to the console when num is equal to 0 then exits.
            console.log('DONE!')
            clearInterval(intervalId)
        }

    }, 1000)



}

// countdown(10)

/*
10
9
8
7
6
5
4
3
2
1
DONE!
*/


/*
randomGame

Write a function called randomGame that selects a random number between 0 and 1 every 1000 milliseconds and each time that a random number is picked, add 1 to a counter. If the number is greater than .75, stop the timer and console.log the number of tries it took before we found a number greater than .75.

*/


const randomGame = () => {

    let counter = 1 //Keeps tract of how many attempts it takes to find a number greater than 0.75

    const intervalId = setInterval(function () {

        //Generates a random number between 0 and 1, rounded to 2 decimals every one second.
        const randomNumber = Math.round(Math.random() * 100) / 100

        //
        if (randomNumber < 0.75) {

            // Increments counter by 1 every second as long as randomNumber is less than 0.75
            counter++

            //Logs randomNumber to the console every 1 second
            console.log(randomNumber)
        } else {

            console.log(randomNumber) // Logs the number greater than 0.75 to the console.


            //Displays the number of attempts it took before finding a number grater than 0.75
            console.log(`\n\nIt took ${counter} ${counter > 1 ? 'tries' : 'try'} before we found a number greater than 0.75`)

            //Stops the interval and exits the function when randomNumber is greater than 0.75
            clearInterval(intervalId)

        }

    }, 1000)



}


randomGame()
