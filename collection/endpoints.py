"""
A file which contains different endpoints and the proper data requirements
"""

total_collection_query_end = 'limit 500; sort id asc;'

GAMES = (
    'https://api.igdb.com/v4/games',
    'fields name, aggregated_rating, category, game_modes, genres, involved_companies, keywords, language_supports, multiplayer_modes,'
    'platforms, player_perspectives, rating, themes, age_ratings;'
)

GAMES_TEXT_DATA = (
    'https://api.igdb.com/v4/games',
    'fields name, storyline, summary'
)

THEMES = (
    'https://api.igdb.com/v4/themes',
    'fields name;'
)

PLATFORM = (
    'https://api.igdb.com/v4/platforms',
    'fields name, category, generation;'
)

GAME_MODES = (
    'https://api.igdb.com/v4/game_modes',
    'fields name;'
)

TIME_TO_BEAT = (
    'https://api.igdb.com/v4/game_time_to_beats',
    'fields hastily, normally, completely;'
)

GENRE = (
    'https://api.igdb.com/v4/genres',
    'fields name;'
)

COMPANIES = (
    'https://api.igdb.com/v4/companies',
    'fields name, changed_company_id;'
)

KEYWORDS = (
    'https://api.igdb.com/v4/keywords',
    'fields name;'
)

LANGUAGE = (
    'https://api.igdb.com/v4/languages',
    'fields name;'
)

MULTIPLAYER = (
    'https://api.igdb.com/v4/multiplayer_modes',
    'fields, campaigncoop'
)

POV = (
    'https://api.igdb.com/v4/player_perspectives',
    'fields, name'
)