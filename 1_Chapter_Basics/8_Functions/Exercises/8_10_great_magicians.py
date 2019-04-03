magicians = [
    'harry houdini',
    'give vernon',
    'uri geller',
    'david copperfield'
    ]
def show_magicians(names):
    for name in magicians:
        print(name)

def make_great(names):
    #name = ["Great " + name for name in names]
    for name in names:
        nm = "Great " + name.title() + "!"
        print(nm)

show_magicians(magicians)

# harry houdini
# give vernon
# uri geller
# david copperfield

make_great(magicians)

# Great Harry Houdini!
# Great Give Vernon!
# Great Uri Geller!
# Great David Copperfield!
