import re


def stringExists(pattern, input):
    x = re.search(pattern, input)

    if x:
        return True
    else:
        return False 

#print(stringExists("(?: o que você acha| o que vc acha| o que voce acha| qual é a sua opinião| qual eh sua opiniao| qual sua opiniao| qual é sua opinião) sobre a UFBA"," qual é a sua opinião sobre a UFBA"))
