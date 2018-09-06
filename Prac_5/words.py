"""
CP1404/CP5632 Practical - Suggested Solution
Count word occurrences in a string
"""
def main()
    DIFFERENT_WORDS = {}
    user_input = input("Text: ")

    words = user_input.split()
    for word in words:
        occurances = DIFFERENT_WORDS.get(word, 0)
        DIFFERENT_WORDS[word] = occurances + 1

    words = list(DIFFERENT_WORDS.keys())
    words.sort()

    length_words = max((len(word) for word in words))
    for word in words:
        print("{} : {}".format(word.ljust(length_words),  DIFFERENT_WORDS[word]))


main()
