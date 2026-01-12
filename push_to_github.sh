#!/bin/bash
# Helper script to push to GitHub

echo "🚀 Pushing to GitHub..."
echo ""
echo "You'll need to authenticate. Options:"
echo ""
echo "1. Personal Access Token (Recommended):"
echo "   - Go to: https://github.com/settings/tokens"
echo "   - Generate new token with 'repo' permissions"
echo "   - Use token as password when prompted"
echo ""
echo "2. SSH Key (Alternative):"
echo "   - Set up SSH: git remote set-url origin git@github.com:MukamaJ-2/Sign-language-Translator.git"
echo ""
echo "Pushing now..."
echo ""

git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Successfully pushed to GitHub!"
    echo "Visit: https://github.com/MukamaJ-2/Sign-language-Translator"
else
    echo ""
    echo "❌ Push failed. Please check authentication."
    echo ""
    echo "Alternative: Use GitHub CLI"
    echo "  gh auth login"
    echo "  git push -u origin main"
fi
