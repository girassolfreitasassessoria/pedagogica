#!/bin/bash
# deploy.sh - Prepare and push site to GitHub repository girassolfreitas/girassolfreitas
set -e
echo "Preparing deploy for girassolfreitas/girassolfreitas..."

# Ensure we're in the repository root
# Initialize git if needed
if [ ! -d .git ]; then
  git init
  git checkout -b main || git checkout -B main
fi

git add .
git commit -m "Deploy site Girassol Freitas" || echo "No changes to commit."
git remote remove origin || true
git remote add origin https://github.com/girassolfreitas/girassolfreitas.git
echo "Pushing to GitHub (main branch)..."
git push -u origin main --force
echo "Deploy complete. Then in GitHub: Settings -> Pages -> Source: main branch, / (root). Site URL: https://girassolfreitas.github.io/girassolfreitas/"
