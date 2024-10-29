import requests
import time

import pandas as pd

import endpoints
from endpoints import total_collection_query_end as query_end
from utility.update_yaml import retrieve_yaml, save_field



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


def generate_initial_csvs() -> None:
    non_game_cats = [
        endpoints.THEMES, endpoints.PLATFORM, endpoints.GAME_MODES, endpoints.GENRE, endpoints.COMPANIES,
        endpoints.KEYWORDS, endpoints.LANGUAGE, endpoints.POV
    ]

    csv_names = [
        'Themes', 'Platform', 'Game Modes', 'Genre', 'Companies', 'Keywords', 'Language', 'POV'
    ]

    for i, (url, query) in enumerate(non_game_cats):
        curr_query = query
        last_id = 0
        count = 0

        while True:
            # Prevent the lock out from to many calls to quickly
            if count == 3:
                time.sleep(5)
                count = 0

            curr_query += query_end + f'where id > {last_id};'
            response = requests.post(url, headers=headers, data=curr_query)
            data = response.json()

            if 'status' in data[0] and data[0]['status'] >= 400:
                break

            df = pd.DataFrame(data)
            df.to_csv(f'../data/{csv_names[i]}.csv', index=False)

            last_id = df.tail(1)['id']
            curr_query = query
            count += 1

generate_initial_csvs()