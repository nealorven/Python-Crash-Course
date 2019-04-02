def make_album(name_artist, name_album, tracks=''):
    albums = {'artist': name_artist, 'album': name_album}
    if tracks:
        albums['tracks'] = tracks
    return albums

while True:
    print("\nPlease write artist and his album:")
    print("(enter 'q' at any time to quit)")

    n_artist = input("Name of artist: ")
    if n_artist == 'q':
        break
    n_album = input("Name of album: ")
    if n_album == 'q':
        break
    n_track = input("Number of tracks: ")
    if n_album == 'q':
        break

    new_album = make_album(n_artist, n_album, n_track)
    print(f"\nNew album added: {new_album}")

# Name of artist: roma
# Name of album: everest

# New album added: {'artist': 'roma', 'album': 'everest', 'tracks': '21'}

# Please write artist and his album:
# (enter 'q' at any time to quit)
# Name of artist: q
