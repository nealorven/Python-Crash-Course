magicians = [
    'harry houdini',
    'give vernon',
    'uri geller',
    'david copperfield'
    ]
mags_migrate = []

def show_magicians(names):
    for name in magicians:
        print(name)

def make_great(magicians, mags_migrate):
    while magicians:
        migrate = magicians.pop()
        print("Great " + migrate.title())
        mags_migrate.append(migrate)
        # name = ["Great " + name for name in names]

make_great(magicians[:], mags_migrate)

# Great David Copperfield
# Great Uri Geller
# Great Give Vernon
# Great Harry Houdini

show_magicians(magicians)

# harry houdini
# give vernon
# uri geller
# david copperfield
