

class BoggleGame {
    constructor (boardId, secs =60) {
        this.secs = secs;
        this.showTimer()

        this.score = 0;
        this.words = new Set();
        this.board = $("#" + boardId); 


        this.timer = setInterval(this.tick.bind(this), 1000);

        $(".guess", this.board).on("submit", this.handleSubmit.bind(this)); 
    }

    /*showing word in a list of accepted words */
    showWord(word) {
        $(".guess", this.board).append($("<li>", {text: word}));
    }
    /* rendering a message to inform player of status of word*/
    showMessage(msg, cls) {
        $(".msg", this.board).text(msg).removeClass().addClass(`msg ${cls}`)
    }
    /* updates the score as words are added to the list */
    showScore(){
        $(".score", this.board).text(this.score)
    }

   

    /* handling click event. Once submit is clicked, check if word is valid for the words in the board */
    async handleSubmit(evt) {
        evt.preventDefault();
        const $word = $(".word", this.board);
    
        let word = $word.val();
        if (!word) return;

        if (this.words.has(word)) {
            this.showMessage(`Already found ${word}`, "err");
        return;
        }

        /* reaching out to server to check word */
        const resp = await axios.get("/check-word", {params: {word: word}});
        if (resp.data.result === 'not-word'){
            this.showMessage(`${word} is not a valid English word`, 'err');
        }
        else if (resp.data.result === 'not-on-board'){
            this.showMessage(`${word} is not a valid word on this board`, 'err');
        }
        else {
            this.showWord(word);
            this.score += word.length
            this.showScore();
            this.words.add(word);
            this.showMessage(`Added ${word}`, 'ok');
        }
        $word.val('').focus();
    }
    /* function to update time left*/
    showTimer(){
        $(".timer", this.board).text(this.secs)
    }

    // could use some help understanding why this is async below
    /* tick function to lower the secs remaining and clear timer when 0 is reached*/
    async tick() {
        this.secs -= 1
        this.showTimer()

        if (this.secs === 0){
            clearInterval(this.timer)
            await this.scoreGame()
        }
    }
    /* post score at end of game */
    async scoreGame() {
        $(".guess", this.board).hide()
        const resp = await axios.post("/post-score", {score: this.score});
        if (resp.data.brokeRecord) {
            this.showMessage(`Heres your new record: ${this.score}`, "ok");
        }
        else {
            this.showMessage(`Final score: ${this.score}`, "ok")
        }
        
    }
    }