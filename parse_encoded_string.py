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
