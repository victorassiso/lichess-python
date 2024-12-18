import requests

def get_user_rating_history(username: str, perfType: str):
  # Validate input parameters
  if not isinstance(username, str) or not username:
    raise ValueError(f"'username' must be a non-empty string. Got: {username}")
  if not isinstance(username, str) or not username:
    raise ValueError(f"'perfType' must be a non-empty string. Got: {perfType}")

  try:
    response = requests.get(f"https://lichess.org/api/user/{username}/rating-history")
    data = response.json()
    ratings = next((item for item in data if item['name'] == perfType), None)
    return ratings
  except requests.exceptions.RequestException as error:
    print(f"Request failed: {error}")
    raise
  