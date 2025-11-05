#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Run the bot in scheduled mode
python3 bot.py --mode scheduled
