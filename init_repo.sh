#!/usr/bin/env bash

set -e

TARGET_DIR="/opt/render/project/git-target"
REPO_URL="git@github.com:paramshinde/Project.git"

if [ ! -d "$TARGET_DIR/.git" ]; then
  echo "Cloning repository..."
  git clone "$REPO_URL" "$TARGET_DIR"
else
  echo "Repository already exists"
fi
