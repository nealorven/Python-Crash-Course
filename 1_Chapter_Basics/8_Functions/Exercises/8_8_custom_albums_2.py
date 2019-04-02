def make_album(name_artist, name_album, tracks=''):
    album = {'artist': name_artist, 'album': name_album}
    if tracks:
        album['tracks'] = tracks
    return album

def get_formatted_album(name_artist, name_album, tracks=''):
    if tracks:
        get_album = f"{name_artist}, {name_album}, {tracks}"
    else:
        get_album = f"{name_artist}, {name_album}"
    return get_album.title()

while True:
    print("\nPlease write artist and his album:")
    print("(enter 'q' at any time to quit)")

    n_artist = input("Name of artist: ")
    if n_artist == 'q':
        break
    n_album = input("Name of album: ")
    if n_album == 'q':
        break
    n_track = int(input("Number of tracks: "))
    if n_album == 'q':
        break
    new_album = make_album(n_artist, n_album, n_track)
    print(f"\nNew album added: {new_album}")

    answer = input("Want to see saved albums? yes/no")
    if answer == 'yes':
        pass
    else:
        print("You entered an incorrect answer.")

# Name of artist: roman
# Name of album: everest
# Number of tracks: 21

# New album added: {'artist': 'roman', 'album': 'everest', 'tracks': 21}

# Please write artist and his album:
# (enter 'q' at any time to quit)
# Name of artist: q

# Sorted: John, Hooker, 21
