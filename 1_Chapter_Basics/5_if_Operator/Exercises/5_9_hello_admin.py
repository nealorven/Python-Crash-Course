### For sequences, (strings, lists, tuples),
### use the fact that empty sequences are false:

# Recommended to use:
# if not seq:
# if seq:

# Not Recommended:
# if len(seq):
# if not len(seq):

names = []
if not names:
    print("We need to find some users!")

# We need to find some users!
