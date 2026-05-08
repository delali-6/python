#This program is designed to check the strength of a password entered by the user. 
# The program will evaluate the password based on certain criteria such as length, use of 
# uppercase and lowercase letters, numbers, and special characters. The user will be prompted to 
# enter a password, and the program will provide feedback on the strength of the password, categorizing 
# it as weak, moderate, or strong based on the criteria met. This helps users create more secure passwords 
# to protect their accounts and personal information.
import re
password = input("Enter a password to check its strength: ")
if len(password) < 6:
    print("Your password is weak. It should be at least 6 characters long.")
elif len(password) < 10:
    print("Your password is moderate. It should be at least 10 characters long.")
else:
    print("Your password is strong. It is at least 10 characters long.")
if not re.search(r"[A-Z]", password):
    print("Your password should contain at least one uppercase letter.")
if not re.search(r"[a-z]", password):
    print("Your password should contain at least one lowercase letter.")
if not re.search(r"[0-9]", password):
    print("Your password should contain at least one number.")
if not re.search(r"[!@#$%^&*(),.?/\":{}|<>]", password):
    print("Your password should contain at least one special character.")