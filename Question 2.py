def vowels_words(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

text = "Anant Bhatt"
print("Number of vowels:  ",vowels_words(text))