import string, random
import os

def generatePassword(num):
    password = ''

    for n in range(num):
        x = random.randint(0, 94)  # all characters excpet \n \t etc
        password += string.printable[x]
    
    return password

# clears the console output
def clear():
    os.system('clear')

def main():
    print("======================")
    print(" Password Generator ")
    print("======================\n")
    print("Please enter the password length.\n")
    success = False
    while (not success):
        
        try:
            length = input("Length: ")
            lengInt = int(length)
            success = True
        except ValueError:
            print("****************************")
            print("Please enter a valid number.")
            print("****************************")


if __name__ == "__main__":
    main()