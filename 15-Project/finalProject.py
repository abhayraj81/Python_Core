#           password strength checker

# Objective:
# The objective is to build a Password Strength Checker that evaluates the strength of user - provided password based on common security criteria. The program helps users create secure passwords by providing feedback on password quality and suggesting improvements.

# password strength check conditions:
# min 8 chars, digit, uppercase, lowercase, special char

import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak : password length must be at least 8 char"
    
    if not any(char.isdigit() for char in password):
        return "Weak : password must contain a digit"
    
    if not any(char.isupper() for char in password):
        return "Weak : password must contain an upper char"
    
    if not any(char.islower() for char in password):
        return "Weak : password must contain an lower char"
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Medium: Add special characters to make your password stronger."

    return "Strong : Your password is secured!"


def password_checker():
    print("Welcome to the password strength checker")

    while True:
        password = input("\nEnter your password (or type 'exit' to Quit) : ")

        if password.lower() == 'exit':
            print("Thank you using Password Strength Checker")
            break

        result = check_password_strength(password)
        print(result)


# Run the Password Strenth Checker Tool
if __name__ == "__main__":
    password_checker()
    


