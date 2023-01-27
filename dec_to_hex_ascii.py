def dec_to_hex(text):
    result = ''
    for el in text:
        if el == ' ':
            result += '\n'
        i = hex(ord(el))
        result += i + ' '

    result.rstrip()
    return result


inp = "My name is Alex"
print(dec_to_hex(inp))