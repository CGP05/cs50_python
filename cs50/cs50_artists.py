import requests

def get_artists(query, limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/agent/search", {"q": query, "limit"}
        )
        response.raise_for_status()
    except requests.HTTPError:
        return []

    content = response.json()
    return [artist["title"] for artist in agent["data"]]
