import string, random
import os
import pyperclip

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
            print("****************************\n")

    clear()
    password = generatePassword(int(length))
    print("Your generated password is:")
    print(password)
    decisionSuccess = False
    # promts the user to either copy pw to clipboard or not
    while (not decisionSuccess):

        decision = input("Do you want to copy to clipboard? [y/n]")
    
        if (decision == 'n' or decision == "no"):
            print("Okay, bye.")
            decisionSuccess = True
    
        elif(decision == 'y' or decision == "yes"):
            pyperclip.copy(password)
            print("Password has been copied to clipboard.")
            decisionSuccess = True

        else:
            print("please type either \"y/yes\" or \"n/no\"")



if __name__ == "__main__":
    main()