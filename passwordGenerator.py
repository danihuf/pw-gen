import string, random

def generatePassword(num):
    password = ''

    for n in range(num):
        x = random.randint(0, 94)  # all characters excpet \n \t etc
        password += string.printable[x]
    
    return password
