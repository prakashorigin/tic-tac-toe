#!/bin/bash

# Tic Tac Toe - Quick Start Script

echo "🎮 Tic Tac Toe Game - Quick Start"
echo "=================================="
echo ""

# Check Python version
echo "✅ Checking Python installation..."
python3 --version

echo ""
echo "Select what you want to do:"
echo "1. Play console version"
echo "2. Start web server (localhost:5000)"
echo "3. Install dependencies for web version"
echo "4. Show git status"
echo "5. Exit"
echo ""

read -p "Enter your choice (1-5): " choice

case $choice in
    1)
        echo ""
        echo "🎮 Starting Tic Tac Toe Console Game..."
        python3 tic_tac_toe.py
        ;;
    2)
        echo ""
        echo "🌐 Installing dependencies (if needed)..."
        pip3 install -q -r requirements.txt
        echo ""
        echo "✅ Starting Web Server..."
        echo "📱 Open http://localhost:5000 in your browser"
        echo "Press Ctrl+C to stop the server"
        echo ""
        python3 app.py
        ;;
    3)
        echo ""
        echo "📦 Installing dependencies..."
        pip3 install -r requirements.txt
        echo "✅ Dependencies installed!"
        ;;
    4)
        echo ""
        git status
        echo ""
        echo "Recent commits:"
        git log --oneline -5
        ;;
    5)
        echo "Goodbye! 👋"
        ;;
    *)
        echo "Invalid choice. Exiting."
        ;;
esac
