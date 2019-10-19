def invert_string(a_string):
    return a_string[::-1]


a_string = input('word?')
print(invert_string)

def is_palindrom(a_string):
    return a_string == a_string[::-1]
