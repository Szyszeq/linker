import random
import string

def randomizer(length):
    """ Generuje randomowy ciąg znaków okreslonej dlugosci."""
    znaki = string.ascii_letters + string.digits + "!@#$%&"
    return ''.join(random.choice(znaki) for i in range(length))

linksDict={}
while exit != 1:
    decision = input("Hey there! If you want to generate a new link, type L. If you want to look for your link type S. If you want to exit type E :)")
    if decision.lower() == "l":
        userLink = input("Please enter the link you want to shorten:")
        linksDict["userLink"] = "http://linker.py/" + randomizer(6)
        print(linksDict.get(userLink))
    elif decision.lower() == "s":
        userLink = input("Please enter your link:")
        if userLink in linksDict:
            print("Your link is:" + linksDict.get(userLink))
        else:
            print("We don't have that link yet :(")
    elif decision.lower() == "e":
        print("See you soon!")
        break
    else:
        print("Wrong command, try again!")
