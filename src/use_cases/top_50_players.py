from api.get_one_leaderboard import get_one_leaderboard

def print_top_50_classical_players():
  top_50_players = get_one_leaderboard(50, 'classical')

  print('Top 50 classical chess players:\n')
  for index, player in enumerate(top_50_players, start=1):
    username = player['username']
    print(f"{index}º: {username}")