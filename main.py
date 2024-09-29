import random
import string
import pyperclip

def generate_password(length, include_uppercase=True, include_numbers=True, include_symbols=True):
    # Define the character sets based on the options selected
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase else ""
    numbers = string.digits if include_numbers else ""
    symbols = string.punctuation if include_symbols else ""
    
    all_characters = lower + upper + numbers + symbols
    
    if not all_characters:
        raise ValueError("No character types selected to generate the password.")

    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Secure Password Generator!")
    
    try:
        length = int(input("Enter the desired password length: "))
        include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, include_uppercase, include_numbers, include_symbols)
        print(f"\nGenerated Password: {password}")
        
        # Optionally copy the password to clipboard
        copy_to_clipboard = input("Do you want to copy the password to the clipboard? (y/n): ").lower() == 'y'
        if copy_to_clipboard:
            pyperclip.copy(password)
            print("Password copied to clipboard!")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
