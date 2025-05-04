def iso_words(words):
    words = words.lower()
    return len(set(words)) == len(words)

print(iso_words("Anant"))
print(iso_words("Virat"))