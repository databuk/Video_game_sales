def clean_data(data):
    data.columns = data.columns.str.lower().to_list()
    data.drop(columns=['id', 'year'], inplace=True, errors='ignore')
    data.console.replace({'ds': 'Nintendo DS',
'wii': 'Nintendo Wii',
'pc': 'Personal Computer',
'ps2': 'PlayStation 2',
'ps3': 'PlayStation 3',
'psp': 'PlayStation Portable',
'x': 'XB',
'x360': 'Xbox 360',
'psv': 'PlayStation Vita',
'gba': 'Game Boy Advance',
'gc': 'GameCube',
'pc': 'PlayStation 1',
'wiiu': 'Nintendo Wii U',
'xone': 'Xbox One',
'ps4': 'PlayStation 4',
'3ds': 'Nintendo 3DS',
'dc': 'Dreamcast'}, inplace=True)
    data.rating.replace({'E' : 'Everyone', 'E10+': 'Everyone 10 and Older', 
                    'M': 'Mature 17+', 'T': 'Teen', 'K-A': 'Everyone', 'RP': 'Rating Pending'}, inplace=True)
    return data
    