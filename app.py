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



