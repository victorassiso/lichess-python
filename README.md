# Lichess API Challenge

This project is part of a job selection process and consists of a Python application that interacts with the Lichess API to collect and analyze chess player data.

## Features

The project has three main functionalities:

1. List the top 50 classical chess players
2. Display the rating history for the last 30 days of the top 1 player
3. Generate a CSV file with the last 30 days rating history of the top 50 players

## Requirements

- Python 3.10
- Python packages listed in `requirements.txt`

## Getting Started

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Run the project
```bash
python ./src/main.py
```

## Output

- The list of top 50 players will be displayed in the console
- The rating history of the #1 player will be displayed in the console
- A CSV file will be generated at `data/output.csv` with the last 30 days rating history of the top 50 players
