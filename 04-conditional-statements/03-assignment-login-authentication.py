# Login Authentication using conditional statements. Assume you have predefined username and password

# WAP that prompts the user to enter a username and password and check whethr they match. Provide appropriate messages for the following cases.
# Both username and password are correct.
# Username is correct but password is incorrect .
# Username is incorrect.

predefined_username = "Abhay81"
predefined_password = "Pass@101"

username = input("Enter Username : ")
password = input("Enter Password : ")
if (predefined_username == username) and (predefined_password == password):
    print("Login Succesfull !")
elif (predefined_username == username) and (predefined_password != password):
    print("Invalid password !")
else:
    print("Invalid Credentials !")



