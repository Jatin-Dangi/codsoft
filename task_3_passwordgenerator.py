import string
import random

def create_password(length):
    # Define the characters to use for generating the password
    allowed_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(allowed_characters) for _ in range(length))
    
    return password

def main():
    try:
        # Prompt the user to enter the desired password length
        length = int(input("Enter the desired password length: "))
        
        # Check if the entered length is valid
        if length < 1:
            print("Password length should be at least 1.")
        else:
            # Generate the password using the create_password function
            password = create_password(length)
            
            # Print the generated password
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
