#!/usr/bin/env bash

# nbstripout source/*

### Remove all old notebooks
echo 'Remove old folder...'
rm -rf notebooks
mkdir -p notebooks

### Perform cleaning
echo 'Start cleaning...'
python scripts/clean_notebooks.py notebooks_src
