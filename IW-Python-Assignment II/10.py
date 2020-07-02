# 10. Write a function that takes camel-cased strings (i.e. ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument, separator, so it will also convert to the kebab
# case (i.e.this-is-camel-case) as well.

# case 1: converting camel-cased to snake_cased
def conversion_wihout_separator(string):
    lst = [string[0].lower()]
    for i in range(1, len(string)):
        if string[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            lst.append('_')
            lst.append(string[i].lower())
        else:
            lst.append(string[i])
    return ''.join(lst)


example = "ThisIsCamelCased"

print(conversion_wihout_separator(example))


# case 2: function with argument separator

def conversion_with_separator(string, separator):
    lst2 = [string[0].lower()]
    for i in range(1, len(string)):
        if string[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            lst2.append(separator)
            lst2.append(string[i].lower())
        else:
            lst2.append(string[i])
    return ''.join(lst2)


print(conversion_with_separator(example, '-'))
