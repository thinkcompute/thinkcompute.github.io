#!/bin/bash

echo "Starting Jupyter Book watcher..."
echo "Watching: think_and_compute/"
echo "Press Ctrl+C to stop"
echo ""

echo "Performing initial build..."
jupyter-book build think_and_compute

watchmedo shell-command \
    --patterns="*.md;*.ipynb;*.py;*.yml;*.yaml;*.bib" \
    --recursive \
    --command='echo "Changes detected, rebuilding..." && jupyter-book build think_and_compute' \
    think_and_compute/