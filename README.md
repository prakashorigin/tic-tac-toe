# Tic Tac Toe Game in Python

A console-based and web-based Tic Tac Toe game built using Python.

## Features
- ✅ Player vs Computer gameplay
- ✅ Random computer moves
- ✅ Win and tie detection
- ✅ Console version for terminal play
- ✅ Web version with Flask for browser access on localhost

## Project Structure
```
tic-tac-toe/
├── tic_tac_toe.py         # Console-based game
├── app.py                 # Flask web app for localhost
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## How to Run

### Console Version
```bash
python tic_tac_toe.py
```

### Web Version (Localhost)
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Flask app:
```bash
python app.py
```

3. Open your browser and go to:
```
http://localhost:5000
```

## Game Rules
- Players take turns entering positions 1-9
- Positions are numbered:
```
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
```
- First to get 3 in a row (horizontally, vertically, or diagonally) wins
- If all positions are filled with no winner, it's a tie

## Technologies Used
- Python 3
- Flask (for web version)
- HTML/CSS (for web interface)

## Author
Prakash

## License
MIT License
