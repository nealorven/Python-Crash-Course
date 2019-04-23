# 213
# Сбой теста


def get_formatted_name(first, middle, last):
    """Строит отформатированное полное имя."""
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()

# ОТРИЦАТЕЛЬНО

# E
# ======================================================================
# ERROR: test_first_last_name (__main__.NamesTestCase)
# Имена вида 'Janis Joplin' работают правильно?
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "C:\Repository\Python-Crash-Course\1_Chapter_Basics\11_Testing\2_passing_the_test.py", line 16, in test_first_last_name
#     formatted_name = get_formatted_name('janis', 'joplin')
# TypeError: get_formatted_name() missing 1 required positional argument: 'last'
#
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s
#
# FAILED (errors=1)
