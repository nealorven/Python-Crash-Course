magicians = [
    'harry houdini',
    'give vernon',
    'uri geller',
    'david copperfield'
    ]
def show_magicians(magicians):
    mags = magicians
    for mag in mags:
        print(mag)


mags = show_magicians(magicians[:])
print(mags)

# harry houdini
# give vernon
# uri geller
# david copperfield

print(magicians)

# ['harry houdini', 'give vernon', 'uri geller', 'david Copperfield']
