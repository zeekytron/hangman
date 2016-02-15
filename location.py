
def getInputFromUser():
    input = raw_input("what state are you from? ")
    if input == "":
        print "I don't understand that answer."
        return getInputFromUser()
    else:
        return input


def checkifIhavebeentothisstate (state):
    statesIHaveBeenIn = ["wisconsin" , "michigan" , "illinois"]
    for s in statesIHaveBeenIn:
        if s.lower() == state.lower():
            return True
    return False


Stateyouarefrom = getInputFromUser() #raw_input("what state are you from? ")

if checkifIhavebeentothisstate(Stateyouarefrom):  
    print "hey i have been to %s" % Stateyouarefrom
else:
    print "I havent been to %s, mabye I should go there" % Stateyouarefrom


