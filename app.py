from flask import Flask, session, redirect, render_template, jsonify, request 
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = "asjbfakjsk"

boggle_game = Boggle()

@app.route('/')
def homepage():
    """Showing the board"""
    board = boggle_game.make_board()
    session['board']=[]
    return render_template('index.html', board=board)



@app.route("/check-word")
def check_word():
    word = request.args['word']
    board = session['board']
    response = boggle_game.check_valid_word(board, word)
    return jsonify({"result": response})

