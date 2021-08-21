import re


def stringExists(pattern, input):
    x = re.search(pattern, input)

    if x:
        return True
    else:
        return False 
