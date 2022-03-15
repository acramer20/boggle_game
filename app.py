from crypt import methods
from flask import Flask, session, redirect, render_template, jsonify, request 
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = "asjbfakjsk"

boggle_game = Boggle()

@app.route('/')
def homepage():
    """Showing the board"""
    board = boggle_game.make_board()
    session['board']= board
    return render_template('index.html', board=board)

@app.route("/check-word")
def check_word():
    """checking if word is in dictionary/board"""
    word = request.args['word']
    board = session['board']
    response = boggle_game.check_valid_word(board, word)
    return jsonify({"result": response})

@app.route("/post-score", methods=["POST"])
def post_score():
    """recording the score, num of times played, and updating the highscore if reached"""
    score = request.json["score"]
    num_plays = session.get("num_plays", 0)
    highscore = session.get("highscore", 0)

    session['num_plays'] = num_plays + 1
    session['highscore'] = max(score, highscore)
    
    return jsonify(brokeRecord=score > highscore)



