import requests
from utility.update_yaml import retrieve_yaml, save_field
import endpoints

headers ={
        'Client-ID': retrieve_yaml('client_id'),
        'Authorization': f'Bearer {retrieve_yaml("access_token")}'
    }

def update_access_token() -> None:
    """
    Gets a access token and save it
    :return:
    """
    url = 'https://id.twitch.tv/oauth2/token'

    params = {
        'client_id': retrieve_yaml('client_id'),
        'client_secret': retrieve_yaml('client_secret'),
        'grant_type': 'client_credentials'
    }

    response = requests.post(url, params=params)
    save_field(response.json())


def grab_games() -> None:
    url = 'https://api.igdb.com/v4/games'
    last_id = 0

    query = ('fields aggregated_rating, category, game_modes, genres, involved_companies, keywords, multiplayer_modes, name, platforms, player_perspectives, rating, storyline, summary, themes;'
             'limit 1;'
             'sort id asc;'
             f'where id > {last_id};')


    response = requests.post(url, headers=headers, data=query)
    data = response.json()

def grab_data(url: str, query: str) -> None:
    last_id = 0

    query = query + f'where id > {last_id};'

    response = requests.post(url, headers=headers, data=query)
    data = response.json()
    print(data)


