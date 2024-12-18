import sys 
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from src.use_cases.top_50_players import print_top_50_classical_players
from src.use_cases.last_30_days_rating_history import print_last_30_day_rating_for_top_player
from src.use_cases.top_50_players_last_30_days_rating_history import generate_rating_csv_for_top_50_classical_players

print_top_50_classical_players()
print('')
print_last_30_day_rating_for_top_player()
print('')
generate_rating_csv_for_top_50_classical_players()