gamesIlike = ["minecraft" , "terraria" , "dragonvale"]
def getInputFromUser():
    input = raw_input("what game do you like? ")
    if input == "":
        print "I don't understand that answer."
        return getInputFromUser()
    if input == ""  or "   ":
        print "please type a a letter or one space for words"
        return getInputFromUser()
    else:
        return input


def checkifIlikethisgame (game):
    gamesIlike = ["minecraft" , "terraria" , "dragonvale"]
    for g in gamesIlike:
        if g.lower() == game.lower():
            return True
    return False


Gamesyoulike = getInputFromUser() #raw_input("what game do you like? ")

if checkifIlikethisgame(Gamesyoulike):  
    print "hey i have played %s" % Gamesyoulike
else:
    print "I have not played %s, mabye I should play that game" % Gamesyoulike



