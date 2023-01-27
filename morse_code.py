class Morse:
    __morse_dict = {
        "A": "·-", "B": "-···", "C": "-·-·",
        "D": "-··", "E": "·", "F": "··-·",
        "G": "--·", "H": "-··", "I": "····",
        "J": "·---", "K": "-·-", "L": "·-··",
        "M": "--", "N": "-·", "O": "---",
        "P": "·--·", "Q": "--·-", "R": "·-·",
        "S": "···", "T": "-", "U": "··-",
        "V": "···-", "W": "·--", "X": "-··-",
        "Y": "-·--", "Z": "--··",
        "1": "·----", "2": "··---", "3": "···--",
        "4": "····-", "5": "·····", "6": "-····",
        "7": "--···", "8": "---··", "9": "----·",
        "0": "-----",
        ".": "·-·-·-", ",": "--··--", "?": "··--··",
        " ": " "
    }

    def __init__(self, txt):
        self.__code_txt = txt.upper()
        # print(self.__code_txt)
        self.__code_res = ""

    def __coder(self):
        for ch in self.__code_txt:
            for key in self.__morse_dict.keys():
                if ch == key == " ":
                    self.__code_res += "\n"
                elif ch == key:
                    # print(ch, key, sep=";")
                    self.__code_res += self.__morse_dict[key]
                    self.__code_res += " "
                    # print(self.__code_res)

    def __str__(self):
        self.__coder()
        return self.__code_res


var = True
count = 0
while var:
    code = str(input("Write a text you want to code:"))
    for i in code.upper():
        if i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.,? ":
            count += 1
    if count:
        print("Write a good text, please")
        count = 0
    else:
        var = False

code_obj = Morse(code)
print(code_obj)


