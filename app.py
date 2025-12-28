"""
Tic Tac Toe Web Game - Flask Application
Run with: python app.py
Access at: http://localhost:5000
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Add security headers
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

# Game state
game_state = {
    "board": [" "] * 9,
    "current_player": "X",
    "game_over": False,
    "winner": None
}

def reset_game():
    game_state["board"] = [" "] * 9
    game_state["current_player"] = "X"
    game_state["game_over"] = False
    game_state["winner"] = None

def check_win(player):
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
        (0, 4, 8), (2, 4, 6)               # diagonals
    ]
    for combo in win_combinations:
        if game_state["board"][combo[0]] == game_state["board"][combo[1]] == game_state["board"][combo[2]] == player:
            return True
    return False

def check_tie():
    return " " not in game_state["board"]

def get_computer_move():
    """Get the best move for computer (using random strategy)"""
    available_moves = [i for i in range(9) if game_state["board"][i] == " "]
    if available_moves:
        return random.choice(available_moves)
    return None

@app.route("/")
def index():
    reset_game()
    return render_template("index.html")

@app.route("/api/move", methods=["POST"])
def make_move():
    data = request.json
    position = data.get("position")
    
    # Validate move
    if position < 0 or position > 8 or game_state["board"][position] != " ":
        return jsonify({"error": "Invalid move"}), 400
    
    # Player move
    game_state["board"][position] = "X"
    
    # Check if player won
    if check_win("X"):
        game_state["game_over"] = True
        game_state["winner"] = "player"
        return jsonify({
            "board": game_state["board"],
            "game_over": True,
            "winner": "You Win! 🎉"
        })
    
    # Check if tie
    if check_tie():
        game_state["game_over"] = True
        game_state["winner"] = "tie"
        return jsonify({
            "board": game_state["board"],
            "game_over": True,
            "winner": "It's a Tie! 🤝"
        })
    
    # Computer move
    comp_move = get_computer_move()
    if comp_move is not None:
        game_state["board"][comp_move] = "O"
        
        # Check if computer won
        if check_win("O"):
            game_state["game_over"] = True
            game_state["winner"] = "computer"
            return jsonify({
                "board": game_state["board"],
                "game_over": True,
                "winner": "Computer Wins! 💻",
                "computer_move": comp_move
            })
        
        # Check if tie
        if check_tie():
            game_state["game_over"] = True
            game_state["winner"] = "tie"
            return jsonify({
                "board": game_state["board"],
                "game_over": True,
                "winner": "It's a Tie! 🤝",
                "computer_move": comp_move
            })
    
    return jsonify({
        "board": game_state["board"],
        "game_over": False,
        "winner": None,
        "computer_move": comp_move
    })

@app.route("/api/reset", methods=["POST"])
def reset():
    reset_game()
    return jsonify({
        "board": game_state["board"],
        "game_over": False,
        "winner": None
    })

@app.route("/api/state", methods=["GET"])
def get_state():
    return jsonify({
        "board": game_state["board"],
        "game_over": game_state["game_over"],
        "winner": game_state["winner"]
    })

if __name__ == "__main__":
    print("🎮 Tic Tac Toe Game Starting...")
    print("📱 Open http://localhost:5000 in your browser")
    app.run(debug=True, port=5000)
