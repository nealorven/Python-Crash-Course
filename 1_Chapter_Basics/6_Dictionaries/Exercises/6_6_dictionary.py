intervieweds = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }
not_intervieweds = [
    'roma', 'yana', 'vika', 'misha',
    'jen', 'sarah', 'edward', 'phil'
    ]
for not_interviewed in not_intervieweds:
    if not_interviewed in intervieweds:
        print("{}, thank you for participating in the survey."
            .format(not_interviewed.title()))
    else:
        print("{}, we invite you to take a survey!"
            .format(not_interviewed.title()))

# Roma we invite you to take a survey!
# Yana we invite you to take a survey!
# Vika we invite you to take a survey!
# Misha we invite you to take a survey!
# Jen, thank you for participating in the survey.
# Sarah, thank you for participating in the survey.
# Edward, thank you for participating in the survey.
# Phil, thank you for participating in the survey.
