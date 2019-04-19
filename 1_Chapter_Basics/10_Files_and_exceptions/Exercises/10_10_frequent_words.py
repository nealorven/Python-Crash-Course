
with open('frequent_words.txt') as file_obj:
    content = file_obj.read()
    count = content.count('the')
    print(f"Count: {count} words")

# Count: 18 words
