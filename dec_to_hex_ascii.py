# You need to write a function in Python that accepts a string of ASCII characters.
# It should return each character’s value as a hexadecimal string.
# Separate each byte by a space, and return all alpha hexadecimal characters as lowercase.

def dec_to_hex(text):
    result = ''
    for el in text:
        if el == ' ':
            result += '\n'
        i = hex(ord(el))
        result += i + ' '

    result.rstrip()
    return result


inp = "My name is Ben"
print(dec_to_hex(inp))