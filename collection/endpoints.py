"""
A file which contains different endpoints and the proper data requirements
"""

total_collection_query_end = 'limit 500; sort id asc;'

games = (
    'https://api.igdb.com/v4/games',
    'fields aggregated_rating, category, game_modes, genres, involved_companies, keywords, multiplayer_modes, name, platforms, player_perspectives, rating, storyline, summary, themes;'
)

themes = (
    'https://api.igdb.com/v4/themes',
    'fields name;'
)

platform = (
    'https://api.igdb.com/v4/platforms',
    'fields name, category, generation;'
)

game_modes = (
    'https://api.igdb.com/v4/game_modes',
    'fields name;'
)

time_to_beat = (
    'https://api.igdb.com/v4/game_time_to_beats',
    'fields hastily, normally, completely;'
)

genre = (
    'https://api.igdb.com/v4/genres',
    'fields name;'
)

companies = (
    'https://api.igdb.com/v4/companies',
    'fields name, changed_company_id;'
)

keywords = (
    'https://api.igdb.com/v4/keywords',
    'fields name;'
)

language = (
    'https://api.igdb.com/v4/languages',
    'fields name;'
)

multiplayer = (
    'https://api.igdb.com/v4/multiplayer_modes',
    'fields, campaigncoop'
)

pov = (
    'https://api.igdb.com/v4/player_perspectives',
    'fields, name'
)