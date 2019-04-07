def make_album(name_artist, name_album, tracks=''):
    album = {'artist': name_artist, 'album': name_album}
    if tracks:
        album['tracks'] = tracks
    return album


musician_1 = make_album('john', 'john album')
musician_2 = make_album('neal', 'neal album')
musician_3 = make_album('kenen', 'kenen album')
print(musician_1)
print(musician_2)
print(musician_3)

# {'artist': 'john', 'album': 'john album'}
# {'artist': 'neal', 'album': 'neal album'}
# {'artist': 'kenen', 'album': 'kenen album'}


musician_1 = make_album('john', 'john album', tracks=14)
musician_2 = make_album('neal', 'neal album', tracks=26)
musician_3 = make_album('kenen', 'kenen album', tracks=21)
print(musician_1)
print(musician_2)
print(musician_3)

# {'artist': 'john', 'album': 'john album', 'tracks': 14}
# {'artist': 'neal', 'album': 'neal album', 'tracks': 26}
# {'artist': 'kenen', 'album': 'kenen album', 'tracks': 21}
