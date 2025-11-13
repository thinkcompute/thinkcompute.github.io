#!/bin/bash

echo "Starting Jupyter Book watcher..."
echo "Watching markdown files in: think_and_compute/"
echo "Press Ctrl+C to stop"
echo ""

echo "Performing initial build..."
uv run jupyter-book build think_and_compute

# Watch only markdown files
# --drop: ignore events that occur while the command is running (prevents rebuild loops)
uv run watchmedo shell-command \
    --patterns="*.md" \
    --recursive \
    --drop \
    --command='echo "Changes detected, rebuilding..." && uv run jupyter-book build think_and_compute' \
    think_and_compute/