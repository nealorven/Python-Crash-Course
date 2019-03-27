neal = {
    'first name': 'neal',
    'last name': 'orven',
    'city': 'astana',
    'age': 27
    }
yana = {
    'first name': 'yana',
    'last name': 'neon',
    'city': 'canada',
    'age': 25
    }
den = {
    'first name': 'den',
    'last name': 'ori',
    'city': 'uk',
    'age': 21
    }
people = [
    neal, yana, den
    ]
for person in people:
    for content, description in person.items():
        print("Information request: {} - {}."
            .format(content.capitalize(), str(description).title()))

# Information request: First name - Neal.
# Information request: Last name - Orven.
# Information request: City - Astana.
# Information request: Age - 27.
# Information request: First name - Yana.
# Information request: Last name - Neon.
# Information request: City - Canada.
# Information request: Age - 25.
# Information request: First name - Den.
# Information request: Last name - Ori.
# Information request: City - Uk.
# Information request: Age - 21.
