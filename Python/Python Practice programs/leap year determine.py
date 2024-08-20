'''
To be a leap year
1. The year not ends up with 00:
    leap year if could be fully divided by 4 (no reminder)
2. The year ends up with 00:
    leap year if could be fully divided by 400
    
    
first step by step, easy to understand

year = int(input('Please enter the 4 digit year: '))
if year%400 == 0:
    print('Leap year.')
elif year%100 != 0 and (year%4 == 0):
    print('Leap year.')
else:
    print('Not a leap year.')

Below we define a function to determine

def isLeap(year):
    if year%400 == 0:
        return 'Leap year.'
    elif year%100 != 0 and (year%4 == 0):
        return 'Leap year.'
    else:
        return 'Not a leap year.'

Or:
'''
def isLeap(year):
    if (year%400 == 0 or (year%100 != 0 and year%4 == 0)):
        return 'Leap year.'
    else:
        return 'Not a leap year.'
