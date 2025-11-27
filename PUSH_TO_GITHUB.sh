#!/bin/bash
# 🚀 Quick script to push weed-strain-classifier to GitHub

REPO_NAME="weed-strain-classifier"
USERNAME="tophercook7-maker"
REPO_URL="https://github.com/${USERNAME}/${REPO_NAME}.git"

echo "🚀 Pushing ${REPO_NAME} to GitHub..."
echo ""

# Check if remote exists
if git remote get-url origin &>/dev/null; then
    echo "✅ Remote 'origin' already exists"
    git remote set-url origin ${REPO_URL}
else
    echo "➕ Adding remote 'origin'..."
    git remote add origin ${REPO_URL}
fi

# Ensure we're on main branch
git branch -M main

echo ""
echo "📤 Pushing to GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Successfully pushed to GitHub!"
    echo ""
    echo "🔗 Repository URL:"
    echo "   https://github.com/${USERNAME}/${REPO_NAME}"
    echo ""
    echo "📝 Next steps:"
    echo "   1. Go to: https://github.com/${USERNAME}/${REPO_NAME}/settings/access"
    echo "   2. Add collaborator: ${USERNAME}"
    echo "   3. Upload dataset (see DATASET_SETUP.md)"
    echo "   4. Train model in Colab (see SETUP_INSTRUCTIONS.md)"
    echo "   5. Deploy to Replicate"
else
    echo ""
    echo "❌ Push failed. Make sure:"
    echo "   1. GitHub repo exists at: ${REPO_URL}"
    echo "   2. You have push access"
    echo "   3. Create repo first at: https://github.com/new"
    echo "      Name: ${REPO_NAME}"
fi

