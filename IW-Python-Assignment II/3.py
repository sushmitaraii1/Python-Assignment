# 3. Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text.
from collections import defaultdict


def anagram_checker(paragraph):
    # converting to lower case and removing special characters
    paragraph = paragraph.lower()
    words = paragraph.replace('.', '')

    # converting paragraph to list
    words = words.split()

    # initializing empty dictionary of list
    anagram = defaultdict(list)
    n = 1

    for word in words:

        # converting word to sorted list of word
        c1 = sorted(word)
        # converting sorted word to string
        k = ''.join(c1)

        # if the word is already an anagram to other word, it is skipped
        if k in anagram:
            continue

        # every word is checked with following words in list
        for i in range(0, len(words)):
            c2 = sorted(words[i])
            if c1 == c2:
                # if anagram is found then it is appended at list of given sorted word as a key
                anagram[k].append(words[i])
        n = n + 1

    return anagram


para = "Cat dog tac eat tea god act ogd."
ana = anagram_checker(para)
for key in ana:
    print("The anagram of {} are {}".format(ana[key][0], ana[key]))
