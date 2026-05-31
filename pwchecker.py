#This program is designed to check the strength of a password entered by the user. 
# The program will evaluate the password based on certain criteria such as length, use of 
# uppercase and lowercase letters, numbers, and special characters. The user will be prompted to 
# enter a password, and the program will provide feedback on the strength of the password, categorizing 
# it as weak, moderate, or strong based on the criteria met. This helps users create more secure passwords 
# to protect their accounts and personal information.
def check_password_strength(password: str) -> str:
    
    strength = 0
    #Rules for password strength
    if len(password) >= 8:
        strength += 5
        if any(char.isupper() for char in password):
            strength += 1
        if any(char.islower() for char in password):
            strength += 1
        if any(char.isdigit() for char in password):
            strength += 1
        if any(char in "!@#$%^&£*(),.?/\":{}|<>" for char in password):
            strength += 2
            
            # Categorize password strength and display the result
    if strength <= 3:
        print("Sorry, your password is Weak, try again")
    elif strength == 5 or strength == 6 or strength == 7 or strength == 8:
        print("Getting there, your password is Moderate")
    elif strength >= 9:
        print("Congratulations, your password is Strong")

# Prompt the user to enter a password
user_password = input("Please enter a password to check its strength: ")
# Check the strength of the entered password
check_password_strength(user_password)