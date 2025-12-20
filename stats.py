# counts number of words in a string
def num_words(str):
    words = str.split()
    return len(words)

# counts the characters in a string, capitalization doesn't matter
def count_char(str):
    characters = list(str)
    character_counts = {}
    

    for character in characters:
        lcharacter = character.lower()
        if lcharacter in character_counts:
            character_counts[lcharacter] += 1
        else:
            character_counts[lcharacter] = 1
    return character_counts

