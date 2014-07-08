def ConvertToCelsius (temperature):
    return (int(temperature) - 32)*5/9

def ConvertToFahrenheit (temperature):
    return int(temperature)*9/5 + 32
    

print('Welcome to the temperature converter!')
print('Please choose from the following options')
print('1. Convert fahrenheit to celcius')
print('2. Convert celsius to fahrenheit')
print('3. Enter zipcode')

choice = input('')

if choice == '1' :
    temperature = input('Enter temperature in fahrenheit: ')
    print(round(ConvertToCelsius(temperature),2))
elif choice == '2' :
    temperature = input('Enter temperature in celcius: ')
    print(round(ConvertToFahrenheit(temperature),2))
else:
    print('Invalid choice')