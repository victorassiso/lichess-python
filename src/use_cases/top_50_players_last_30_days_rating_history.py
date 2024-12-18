import sys 
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from datetime import datetime

from src.utils.write_csv_file import write_csv_file
from src.http.get_one_leaderboard import get_one_leaderboard
from src.use_cases.last_30_days_rating_history import get_player_last_30_day_rating

def generate_rating_csv_for_top_50_classical_players():
  # Get Top 50 players in classical chess
  top_50_players = get_one_leaderboard(5, 'classical')
  top_50_players_rating_history = []

  for player in top_50_players:
    # Get player username
    username = player['username']
    
    # Get player last 30 days ratings
    last_30_day_rating = get_player_last_30_day_rating(username)
    
    # Append player rating history to the list
    player_data = {"username": username, **{entry["date"].strftime('%Y-%m-%d'): entry["score"] for entry in last_30_day_rating}}
    top_50_players_rating_history.append(player_data)

  output_path = root / 'data' / 'output.csv'
  write_csv_file(output_path, top_50_players_rating_history)
  print(f"Top 50 players rating history for the last 30 days: File generated at {output_path}")
