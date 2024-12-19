import requests

def get_one_leaderboard(nb: int, perfType: str):
  # Validate input parameters
  if not isinstance(nb, int) or nb <= 0:
    raise ValueError(f"'nb' must be a positive integer. Got: {nb}")
  if not isinstance(perfType, str) or not perfType:
    raise ValueError(f"'perfType' must be a non-empty string. Got: {perfType}")

  try:
    response = requests.get(f"https://lichess.org/api/player/top/{nb}/{perfType}")
    data = response.json()

    # Extract users array from the response
    users = data['users']

    return users
  except requests.exceptions.RequestException as error:
    print(f"Request failed: {error}")
    raise
