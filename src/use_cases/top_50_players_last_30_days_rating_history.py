import os
from utils.write_csv_file import write_csv_file
from api.get_one_leaderboard import get_one_leaderboard
from use_cases.last_30_days_rating_history import get_player_last_30_days_rating_history

def generate_rating_csv_for_top_50_classical_players():
  # Get Top 50 players in classical chess
  top_50_players = get_one_leaderboard(50, 'classical')

  # For each player, get the last 30 days rating history and append it to the list
  top_50_players_last_30_days_rating_history = []
  for player in top_50_players:
    # Get player username
    username = player['username']
    
    # Get player last 30 days rating history
    last_30_days_rating_history = get_player_last_30_days_rating_history(username)
    
    # Append player rating history to the list with its username
    top_50_players_last_30_days_rating_history.append({
      "username": username,
      **{entry["date"].strftime('%Y-%m-%d'): entry["score"] for entry in last_30_days_rating_history}
    })
  
  # Write the list to a CSV file
  current_dir = os.path.dirname(__file__)
  output_path = os.path.join(current_dir, '../data/output.csv')
  write_csv_file(output_path, top_50_players_last_30_days_rating_history)

  print(f"Top 50 players rating history for the last 30 days: File generated at {output_path}")
