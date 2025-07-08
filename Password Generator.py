# A simple Python project for a password generator that creates a new password every 10 seconds. It uses the secrets module for secure random generation and string for character sets.


import secrets
import string
import time

def generate_password(length=16):
    """Generate a secure random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator: A new password will be generated every 10 seconds.")
    try:
        while True:
            new_password = generate_password()
            print(f"New Password: {new_password}")
            time.sleep(10)  # Wait for 10 seconds
    except KeyboardInterrupt:
        print("\nPassword generation stopped. Goodbye!")

if __name__ == "__main__":
    main()


