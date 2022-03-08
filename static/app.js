//ask for clarification on how to 

class BoggleGame {
    constructor (boardId, secs =60) {
        this.secs = secs; 
        this.showTimer();

        this.score = 0;
        this.words = new Set();
        this.board = $("#" + boardId); 
// ----------------- Need to understand where boardId is coming from) and also better understand what showMessage is doing on solution. 
    }
    showWord(word) {
        $(".guess", this.board).append($("<li>", {text: word}));
    }

    showMessage(msg, cls) {
        $(".msg", this.board)
    }

   


    async handleSubmit(evt) {
    
    evt.preventDefault();
    const $word = $(".word", this.board);
    
    let word = $word.val();
    if (!word) return;

    if (this.words.has(word)) {
        this.showMessage(`Already found ${word}`, "err");
        return;
    }

    }
    }