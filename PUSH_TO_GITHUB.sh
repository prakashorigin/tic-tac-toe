#!/bin/bash

# GitHub Push Instructions
# ========================

echo "🚀 PUSHING TO GITHUB..."
echo ""
echo "Repository: https://github.com/prakashorigin/tic-tac-toe"
echo ""

# Check if Git is configured
git config user.name > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "⚠️  Git user not configured. Setting up..."
    git config user.name "Prakash"
    git config user.email "prakash@example.com"
fi

# Check if remote exists
git remote get-url origin > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "⚠️  Remote not configured. Adding..."
    git remote add origin https://github.com/prakashorigin/tic-tac-toe.git
fi

# Show current status
echo "Current Status:"
echo "=============="
git log --oneline -3
echo ""

# Show what will be pushed
echo "About to push:"
echo "=============="
git log origin/main..HEAD --oneline 2>/dev/null || echo "No commits to compare (first push)"
echo ""

# Confirm push
read -p "Ready to push to GitHub? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "Pushing to GitHub..."
    git push -u origin main
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ SUCCESS! Your code is now on GitHub!"
        echo "📱 Visit: https://github.com/prakashorigin/tic-tac-toe"
    else
        echo ""
        echo "⚠️  Push failed. Check your GitHub credentials."
        echo ""
        echo "Troubleshooting:"
        echo "1. Create Personal Access Token: https://github.com/settings/tokens"
        echo "2. Use token as password when prompted"
        echo "3. Or use SSH: https://docs.github.com/en/authentication/connecting-to-github-with-ssh"
    fi
else
    echo "Push cancelled."
fi
