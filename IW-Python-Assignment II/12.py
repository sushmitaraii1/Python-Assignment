# 12. Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.

def is_palindrome(word):
    if word == word[::-1]:
        return "It is palindrome."
    else:
        return "It is not palindrome."


example1 = "tattarrattat"
example2 = "evolution"

print(is_palindrome(example1))
print(is_palindrome(example2))
