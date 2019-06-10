import random
import string
import csv

def randomizer(length):
    """ Generuje randomowy ciąg znaków okreslonej dlugosci z podanego w zmiennej znaki stringa."""
    znaki = string.ascii_letters + string.digits + "!@#$%&?><^"
    return ''.join(random.choice(znaki) for i in range(length))

decision = input("Hey there! If you want to generate a new link, type L. If you want to look for your link type S. If you want to exit type E :)\n")

while exit != 1:

    if decision.lower() == "l":
        userLink = input("Please enter the link you want to shorten: ")
        link = "http://linker.py/" + randomizer(6)
        with open('db.csv', mode='a', newline='') as db:
            db_writer = csv.writer(db, delimiter=',')
            db_writer.writerow([userLink,link])
        print(link)

    elif decision.lower() == "s":
        userLink = input("Please enter your link: ")
        found = False
        with open('db.csv', mode='r') as db:
            db_reader = csv.reader(db, delimiter=',')
            for row in db_reader:
                if row[0] == userLink:
                    found = True
                    print("In our database "+userLink+" is "+row[1]+".")
                    break
                if found == False:
                    print("Sorry, we don't have that link yet.")

    elif decision.lower() == "e":
        print("See you soon!")
        break

    else:
        print("Wrong command, try again!")

    decision = input("So what's next? New link? Type L. Search for link? Type S. Exit? Type E.\n")
