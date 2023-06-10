def remove_char(word,char):
    new_word = word.translate({ord(i): None for i in char})
    return new_word

print(remove_char("ahmedz nabilz mohamedz","z"))