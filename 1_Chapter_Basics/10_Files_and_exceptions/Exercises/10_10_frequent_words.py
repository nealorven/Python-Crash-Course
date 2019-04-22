
with open('frequent_words.txt') as file_obj:
    content = file_obj.read()
    count_words = content.count('the')
    print(f"Count: {count_words} words")

# Count: 18 words
