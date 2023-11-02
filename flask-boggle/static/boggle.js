class BoggleGame {
    // Constructor for initializing the game
    constructor(boardId, secs = 60) {
        this.secs = secs;
        this.score = 0;
        this.words = new Set();
        this.board = $(`#${boardId}`);
        this.timer = setInterval(this.tick.bind(this), 1000);

        // Event delegation for form submission
        this.board.on("submit", ".add-word", this.handleSubmit.bind(this));

        // Show the initial timer
        this.showTimer();
    }

    // Display a word in the list of words
    showWord(word) {
        this.board.find(".words").append($("<li>").text(word));
    }

    // Update the displayed score
    showScore() {
        this.board.find(".score").text(this.score);
    }

    // Display a message with a specific CSS class
    showMessage(msg, cls) {
        this.board.find(".msg").text(msg).removeClass().addClass(`msg ${cls}`);
    }

    // Handle the submission of a word
    async handleSubmit(evt) {
        evt.preventDefault();
        const $word = this.board.find(".word");
        let word = $word.val();

        if (!word) return;

        if (this.words.has(word)) {
            this.showMessage(`Already found ${word}`, "err");
            return;
        }

        // Check with the server for word validity
        const resp = await axios.get("/check-word", { params: { word } });

        if (resp.data.result === "not-word") {
            this.showMessage(`${word} is not a valid English word`, "err");
        } else if (resp.data.result === "not-on-board") {
            this.showMessage(`${word} is not a valid word on this board`, "err");
        } else {
            this.showWord(word);
            this.score += word.length;
            this.showScore();
            this.words.add(word);
            this.showMessage(`Added: ${word}`, "ok");
        }

        $word.val("").focus();
    }

    // Update and display the game timer
    showTimer() {
        this.board.find(".timer").text(this.secs);
    }

    // Handle the ticking of the game timer
    async tick() {
        this.secs -= 1;
        this.showTimer();

        if (this.secs === 0) {
            clearInterval(this.timer);
            await this.scoreGame();
        }
    }

    // Score the game and display the final message
    async scoreGame() {
        this.board.find(".add-word").hide();
        const resp = await axios.post("/post-score", { score: this.score });

        if (resp.data.brokeRecord) {
            this.showMessage(`New record: ${this.score}`, "ok");
        } else {
            this.showMessage(`Final score: ${this.score}`, "ok");
        }
    }
}
