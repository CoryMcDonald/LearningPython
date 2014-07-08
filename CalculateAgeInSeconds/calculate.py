from datetime import datetime, date,time

def getBirthDate(month, day, year):
    if not month.isdigit():
        month = (datetime.strptime(month , '%B')).month
    
    if not day.isdigit():
        day = (datetime.strptime(day , '%A')).day
        
    if not year.isdigit():
        raise Exception("Shoot! You can't have a year that's has letters in it!")
        
    return datetime.strptime(str(month) + '/' + str(day) + '/' + str(year), '%m/%d/%Y')


#Main Program
birthDate = input('Enter your birth date: ')

try:
    birthDate = datetime.strptime(birthDate, '%m/%d/%Y')
except:
    print("Sorry I didn't quite get that! Try entering the following")
    unentered = True
    while unentered == True:
        birthMonth = input('Enter the month you were born: ')
        birthDay = input('Enter the day: ')
        birthYear = input('Enter the year: ')
        try:
            birthDate =  getBirthDate(birthMonth, birthDay, birthYear)
            unentered = False
        except:
            print('Whoops, something went wrong - try again')

if birthDate > datetime.now():
    print('Time Travelers not allowed!')
else:
    print('Woah! You are ' + str((datetime.now() - birthDate).total_seconds()) + ' seconds old!')
