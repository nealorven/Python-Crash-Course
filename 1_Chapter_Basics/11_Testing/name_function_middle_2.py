# Page 214
# Реакция на сбойный тест


def get_formatted_name(first, last, middle=''):
    """Строит отформатированное полное имя."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

# ПОЛОЖИТЕЛЬНО

# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK
