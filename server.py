"""
Simple Tic Tac Toe Web Game - Flask
"""
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__, template_folder='templates', static_folder='templates')

game_state = {
    "board": [" "] * 9,
    "game_over": False,
    "winner": None
}

def check_win(player):
    win_combos = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    return any(game_state["board"][a] == game_state["board"][b] == game_state["board"][c] == player 
               for a, b, c in win_combos)

def check_tie():
    return " " not in game_state["board"]

@app.route("/")
def home():
    game_state["board"] = [" "] * 9
    game_state["game_over"] = False
    game_state["winner"] = None
    return render_template("game.html")

@app.route("/move", methods=["POST"])
def move():
    data = request.get_json()
    pos = data.get("pos")
    
    if game_state["game_over"] or game_state["board"][pos] != " ":
        return jsonify({"error": "Invalid move"}), 400
    
    game_state["board"][pos] = "X"
    
    if check_win("X"):
        game_state["game_over"] = True
        game_state["winner"] = "You Win!"
        return jsonify({"board": game_state["board"], "winner": game_state["winner"]})
    
    if check_tie():
        game_state["game_over"] = True
        game_state["winner"] = "Tie!"
        return jsonify({"board": game_state["board"], "winner": game_state["winner"]})
    
    # Computer move
    empty = [i for i in range(9) if game_state["board"][i] == " "]
    if empty:
        comp_pos = random.choice(empty)
        game_state["board"][comp_pos] = "O"
        
        if check_win("O"):
            game_state["game_over"] = True
            game_state["winner"] = "Computer Wins!"
        elif check_tie():
            game_state["game_over"] = True
            game_state["winner"] = "Tie!"
    
    return jsonify({"board": game_state["board"], "winner": game_state["winner"]})

@app.route("/reset", methods=["POST"])
def reset():
    game_state["board"] = [" "] * 9
    game_state["game_over"] = False
    game_state["winner"] = None
    return jsonify({"board": game_state["board"]})

if __name__ == "__main__":
    print("\n🎮 Tic Tac Toe Game Starting...")
    print("📱 Open: http://localhost:8000\n")
    app.run(host="0.0.0.0", port=8000, debug=False)
