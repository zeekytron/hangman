# get the user to enter their name, store it in a variable
name = raw_input("what is your name? ")
myAge = 11

peopleIKnow = ["Isaac", "Josh", "Vicki", "Evan", "Layla", "bOb"]


# Check to see if I know this person
def checkIfIKnowThisPerson(name):
	# loop over all the people I know to see if I find this person in the list of people I know
	for person in peopleIKnow:
		if person.lower() == name.lower():
			# I found somebody in the list, return True
			return True

	#I got through the whole list and did not find somebody I know, return False
	return False


# print out a message based on whether I know this person or not
if checkIfIKnowThisPerson(name):  
  print "Hello %s" % name
else:  
  print "Stranger Danger!!!!"

