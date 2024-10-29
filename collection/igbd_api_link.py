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


def generate_initial_csvs() -> None:
    """
    Iterates over all non game endpoints of interest and builds csvs of them
    :return: None
    """
    non_game_cats = [
        endpoints.THEMES, endpoints.PLATFORM, endpoints.GAME_MODES, endpoints.GENRE, endpoints.COMPANIES,
        endpoints.KEYWORDS, endpoints.LANGUAGE, endpoints.POV
    ]

    csv_names = [
        'Themes', 'Platform', 'Game Modes', 'Genre', 'Companies', 'Keywords', 'Language', 'POV'
    ]

    for i, (url, query) in enumerate(non_game_cats):
        last_id = 0
        count = 0

        # Prevent the lock out from to many calls to quickly
        if count == 4:
            time.sleep(1)
            count = 0

        query += query_end + f'where id > {last_id};'
        response = requests.post(url, headers=headers, data=query)
        data = response.json()

        df = pd.DataFrame(data)
        df.to_csv(f'../data/{csv_names[i]}.csv', index=False)
        count += 1


def generate_game_csv() -> None:
    """
    Generates the main game CSV for user
    :return: None
    """
    url, query = endpoints.GAMES
    _, text_query = endpoints.GAMES_TEXT_DATA
    last_id = 0
    count = 0
    games = []
    text_info = []

    while True:
        # Prevent the lock out from to many calls to quickly
        if count == 4:
            time.sleep(1)
            count = 0

        # All data that is not heavy text
        curr_query = query + query_end + f'where id > {last_id};'
        response = requests.post(url, headers=headers, data=curr_query)
        game_data = response.json()

        # The few fields which are heavy text
        curr_text_query = text_query + query_end + f'where id > {last_id};'
        response = requests.post(url, headers=headers, data=curr_text_query)
        text_data = response.json()

        # Stop loop when we run out of items
        if not game_data or 'status' in game_data[0] and game_data[0]['status'] >= 400:
            break

        games.extend(game_data)
        text_info.extend(text_data)

        last_id = game_data[-1]['id']
        count += 2

        print(len(games))

    df_game = pd.DataFrame(games)
    df_game.to_csv('../data/Games.csv', index=False)

    df_text = pd.DataFrame(text_info)
    df_text.to_csv('../data/Games Text Data.csv', index=False)

generate_game_csv()