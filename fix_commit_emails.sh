#!/bin/bash
# Script to update all commit emails to match GitHub account

CORRECT_EMAIL="josephmukama67@gmail.com"
CORRECT_NAME="MukamaJ-2"

echo "Updating all commits to use email: $CORRECT_EMAIL"
echo "This will rewrite git history..."

# Export the correct email/name for the filter
export CORRECT_EMAIL
export CORRECT_NAME

# Use git filter-branch to update all commits
git filter-branch -f --env-filter "
export GIT_AUTHOR_EMAIL=\"$CORRECT_EMAIL\"
export GIT_AUTHOR_NAME=\"$CORRECT_NAME\"
export GIT_COMMITTER_EMAIL=\"$CORRECT_EMAIL\"
export GIT_COMMITTER_NAME=\"$CORRECT_NAME\"
" --tag-name-filter cat -- --branches --tags

echo "✓ All commits updated!"
echo "Now force push with: git push -f origin main"
