# Values in the string can be separated by any number of zeros.
# The id is a numeric value but will contain no zeros.
# The function should parse the string
# and return a Python dictionary that contains the first name, last name, and id values.
#
# An example input would be “Robert000Smith000123”.
# The function should return the following using that input:
# { “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }

def parse_str(text):
    string_dict = {
        "first_name": "",
        "last_name": "",
        "id": ""
    }
    text_lst = text.replace("0", " ").split()
    count = 0
    for ent in text_lst:
        if count == 0:
            string_dict["first_name"] = ent
            count += 1
        elif count == 1:
            string_dict["last_name"] = ent
            count += 1
        else:
            string_dict["id"] = ent
    return string_dict


inp = "Robert000Smith000123"
print(parse_str(inp))
