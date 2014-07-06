import random

#Grab male names
maleFirstNamesFile = open('maleFirstName.txt', 'r')
maleFirstNames = []

for name in maleFirstNamesFile:
    maleFirstNames.append(name.split()[0])
    
maleFirstNamesFile.close()

#Grab female names
femaleFirstNamesFile = open('femaleFirstNames.txt', 'r')
femaleFirstNames = []

for name in femaleFirstNamesFile:
    femaleFirstNames.append(name.split()[0])
    
femaleFirstNamesFile.close()

#Grab last names
lastNameFile = open('lastnames.txt', 'r')
lastNames = []

for name in lastNameFile:
    lastNames.append(name.split()[0])
    
lastNameFile.close()

#Generate 10 random names
for x in range(0,10):
    if random.uniform(0,1) == 0:
        firstName = random.choice(maleFirstNames)
    else:
        firstName = random.choice(femaleFirstNames)
    
    lastName = random.choice(lastNames)
    
    print(firstName + " " + lastName)