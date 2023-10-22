
import re

def check_password_strength(password):
    # Minimum length: The password should be at least 8 characters long.
    if len(password) < 8 : 
        # print("Enter minimum 8 charactor of password.")
        return False
    # Contains both uppercase and lowercase letters.
    if not re.search("[A-Z]", password) :
        # print("Enter minimum 1 captital charactor of password.")
        return False
    # Contains both uppercase and lowercase letters.
    if not re.search("[a-z]", password) : 
        # print("Enter minimum 1 small charactor of password.")
        return False
    # Contains at least one digit (0-9).
    if not re.search("[0-9]", password) :
        # print("Enter minimum 1 digit number of password.")
        return False
    # Contains at least one special character (e.g., !, @, #, $, %).
    if not re.search("[!@#$%]", password) : 
        #print("Enter minimum 1 special charactor of password.")
        return False
    
    return True

if __name__ == "__main__":
    password = input("Enter any password to verify its strength : ")
    isValid = check_password_strength(password)

    if isValid : 
        print("Valid Password")
    else : 
        print("Password does not have 1 uppercase, 1 lowercase, 1 digit, 8 charcter length and special charactor like _ @#")
