from datetime import date, timedelta
from http.get_one_leaderboard import get_one_leaderboard
from http.get_user_rating_history import get_user_rating_history

def get_player_last_30_days_rating_history(username: str):  
  # Get player full rating history for classical chess
  rating_history = get_user_rating_history(username, 'Classical')
  ratings = rating_history['points']

  # Get the last 30 days rating history
  #   Not all days are represented in rating_history
  #   We assume that if a player doesn't play, the score stays the same
  #   So, if we don't find the rating for a specific date, we use the first available rating before that date
  today = date(2024, 9, 15) # Assuming today is 2024-09-15
  thirty_days_ago = today - timedelta(days=29)
  date_to_score = {}
  first_available_score = None
  i = len(ratings) - 1
  current_date = today
  # This loop iterates over the rating history in reverse order
  #   It starts from today, and stops in thirty days ago
  #   It adds data to date_to_score dictonary for quick access later
  while(i > 0):
    if (current_date >= thirty_days_ago):
      current_date = date(ratings[i][0], ratings[i][1] + 1, ratings[i][2])
      current_score = ratings[i][3]
      date_to_score[current_date] = current_score
      i -= 1
    else:
      first_available_score = current_score
      break
  
  # Transform the date_to_score dictionary with missing dates into an array of all the last 30 days ratings
  current_date = thirty_days_ago
  current_score = first_available_score
  last_30_days_rating_history = []
  for i in range(30):
    current_date = thirty_days_ago + timedelta(days=i)
    
    if (current_date in date_to_score):
      current_score = date_to_score[current_date]
    else:
      date_to_score[current_date] = current_score
    
    last_30_days_rating_history.append({"date": current_date, "score": current_score})

  # Sort the array by date
  last_30_days_rating_history.sort(key=lambda x: x["date"])
  
  return last_30_days_rating_history

def print_last_30_day_rating_for_top_player():
  # Get Top 1 player in classical chess
  top_1_player = get_one_leaderboard(1, 'classical')
  top_1_player_username = top_1_player[0]['username']

  # Get player last 30 days rating history
  last_30_days_rating_history = get_player_last_30_days_rating_history(top_1_player_username)

  # Print the last 30 days rating history
  print(f"Rating history of top 1 player {top_1_player_username} in classical chess for the last 30 days (assuming today is 2024-09-15):\n")
  for i, record in enumerate(last_30_days_rating_history):
    if (i < 29):
      print(f"today-{29-i}: {record.get('score')}")
    else:
      print(f"today: {record.get('score')}")
