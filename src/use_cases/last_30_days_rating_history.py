import sys 
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from datetime import datetime, timedelta
from src.http.get_one_leaderboard import get_one_leaderboard
from src.http.get_user_rating_history import get_user_rating_history

def get_player_last_30_day_rating(username: str):  
  # Get player rating history
  rating_history = get_user_rating_history(username, 'Classical')
  ratings = rating_history['points']

  # Find the first available rating from 30 days ago or before, and cut out everything before that
  today = datetime(2024, 9, 15).date() # Assuming today is 2024-09-15
  thirty_days_ago = today - timedelta(days=29)
  last_30_day_rating = {}
  first_available_score = None
  i = len(ratings) - 1
  current_date = today
  while(i > 0):
    if (current_date >= thirty_days_ago):
      current_date = datetime(ratings[i][0], ratings[i][1] + 1, ratings[i][2]).date()
      current_score = ratings[i][3]
      last_30_day_rating[current_date] = current_score
      i -= 1
    else:
      first_available_score = current_score
      break
  
  # Print the last 30 days rating history while filling in the missing ratings
  current_date = thirty_days_ago
  current_score = first_available_score
  last_30_day_rating_array = []
  for i in range(30): # last 30 days
    current_date = thirty_days_ago + timedelta(days=i)
    
    if (current_date in last_30_day_rating):
      current_score = last_30_day_rating[current_date]
    else:
      last_30_day_rating[current_date] = current_score
    
    last_30_day_rating_array.append({"date": current_date, "score": current_score})

  last_30_day_rating_array.sort(key=lambda x: x["date"])
  
  return last_30_day_rating_array

  
def print_last_30_day_rating_for_top_player():
  # Get Top 1 player in classical chess
  top_1_player = get_one_leaderboard(1, 'classical')
  top_1_player_username = top_1_player[0]['username']

  # Get player rating history
  last_30_day_rating = get_player_last_30_day_rating(top_1_player_username)

  # Print the last 30 days rating history while filling in the missing ratings
  print(f"Rating history of top 1 player {top_1_player_username} in classical chess for the last 30 days (assuming today is 2024-09-15):\n")
  for i, record in enumerate(last_30_day_rating):
    if (i < 29):
      print(f"today-{29-i}: {record.get('score')}")
    else:
      print(f"today: {record.get('score')}")
