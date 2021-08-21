import re

def stringExists(pattern, input):
    x = re.search(pattern, input)

    if x:
        return True
    else:
        return False


def convert(txt):

    def changeBrackets(x):
        x = x.replace("[","(?: ")
        x = x.replace("]",")?")
        return x
        
    def changePar(x):
        x = x.replace("(","(?: ")
        return x

    txt = changePar(txt)
    txt = changeBrackets(txt)


    txt = txt.replace("?: *","?:(.+)")
    txt = txt.replace("*","(?: (.+))")
    txt = txt.replace(" (?:","(?:")
    txt = txt.replace(")? ",")?")
    txt = txt.replace(") (",")(")
    txt = txt.replace("|","| ")


    return txt


#print(convert("what color is [my|your|his|her] (bright red|blue|green|lemon chiffon) *"))