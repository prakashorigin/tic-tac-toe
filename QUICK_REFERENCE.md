# ⚡ QUICK REFERENCE CARD

## 🎯 QUICK START (Choose One)

```bash
# Option 1: Interactive Menu (Easiest)
bash quick_start.sh

# Option 2: Play Console Game
python3 tic_tac_toe.py

# Option 3: Play Web Game
pip3 install -r requirements.txt
python3 app.py
# Then open http://localhost:5000
```

## 🚀 PUSH TO GITHUB (Choose One)

```bash
# Option 1: Automated Helper (Easiest)
bash PUSH_TO_GITHUB.sh

# Option 2: Manual Push
git push -u origin main
```

## 📂 PROJECT STRUCTURE

```
tic-tac-toe/
├── tic_tac_toe.py           ← Console game
├── app.py                   ← Web server
├── templates/index.html     ← Web interface
├── requirements.txt         ← Dependencies
├── README.md                ← Docs
├── .gitignore               ← Git rules
├── quick_start.sh           ← Launcher
└── PUSH_TO_GITHUB.sh        ← Push helper
```

## 📖 DOCUMENTATION

- **README.md** - What is this project?
- **SETUP_GUIDE.md** - How to set it up?
- **PROJECT_STATUS.md** - Complete checklist
- **This file** - Quick commands

## 🔧 COMMON COMMANDS

```bash
# Check git status
git status

# View commits
git log --oneline -5

# Add changes
git add .

# Commit
git commit -m "Your message"

# Push
git push origin main

# Pull latest
git pull origin main
```

## 🐛 TROUBLESHOOTING

**"Port 5000 already in use"**
```bash
lsof -i :5000
kill -9 <PID>
```

**"Flask not found"**
```bash
pip3 install -r requirements.txt
```

**"Python command not found"**
```bash
# Use python3 instead
python3 tic_tac_toe.py
```

## 🎮 PLAYING THE GAME

**Console Version:**
- Enter a number (1-9) for your move
- Numbers correspond to board positions:
  ```
   1 | 2 | 3
  -----------
   4 | 5 | 6
  -----------
   7 | 8 | 9
  ```

**Web Version:**
- Click any empty cell
- Computer plays automatically
- Click "New Game" to restart

## 🔗 LINKS

- **GitHub Repo**: https://github.com/prakashorigin/tic-tac-toe
- **Get PAT**: https://github.com/settings/tokens
- **Flask Docs**: https://flask.palletsprojects.com/

## ✅ STATUS

- ✅ Local setup complete
- ✅ Console version ready
- ✅ Web version ready (localhost)
- ✅ Git configured
- ⏳ GitHub push pending

**Next Step**: `bash PUSH_TO_GITHUB.sh` or `git push -u origin main`

---

**Quick tip**: Create a virtual environment for cleaner setup:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
