# Page 214
# Реакция на сбойный тест


def get_formatted_name(first, last, middle=''):
    """Строит отформатированное полное имя."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

# ПОЛОЖИТЕЛЬНО

# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
#
# OK
