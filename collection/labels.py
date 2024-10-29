"""
This file contains dictionaries for certain enums which cannot be pulled from the
API and instead are just displayed on a table on the API documentation.
"""

category = {
    0 : 'Main Game',
    1 : 'DLC',
    2 : 'Expansion',
    3 : 'Bundle',
    4 : 'Standalone Expansion',
    5 : 'Mod',
    6 : 'Episode',
    7 : 'Season',
    8 : 'Remake',
    9 : 'Remaster',
    10 : 'Expanded Games',
    11 : 'Port',
    12 : 'Fork',
    13: 'Pack',
    14 : 'Update'
}


status = {
    0 : 'Released',
    2 : 'Alpha',
    3 : 'Beta',
    4 : 'Early Access',
    5 : 'Offline',
    6 : 'Cancelled',
    7 : 'Rumored',
    8 : 'Delisted'
}


labels = ['Age Ratings', 'Category', 'Game Modes', 'Genres', 'Developers',
          'Keywords', 'Multiplayer Modes', 'Name', 'Platforms', 'POV',
          'Rating', 'Story', 'Summary', 'Themes']