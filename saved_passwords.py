import random
import string

def check_strength(password):
    length = len(password)

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = sum([has_upper, has_lower, has_digit, has_symbol])

    print("\n🔍 Password Analysis:")
    print(f"Length: {length}")
    print(f"Uppercase: {'✔' if has_upper else '✖'}")
    print(f"Lowercase: {'✔' if has_lower else '✖'}")
    print(f"Digits: {'✔' if has_digit else '✖'}")
    print(f"Symbols: {'✔' if has_symbol else '✖'}")

    if length >= 10 and score == 4:
        print("Strong Password")
    elif length >= 7 and score >= 3:
        print(" Medium Password")
    else:
        print("❌ Weak Password")

def generate_password(length):
    if length < 6:
        print(" Minimum length should be 6")
        return

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))

    print("\n Generated Password:", password)

    save = input("Save this password? (y/n): ")
    if save.lower() == 'y':
        with open("saved_passwords.txt", "a") as file:
            file.write(password + "\n")
        print("Saved to file")

while True:
    print("\n====== PASSWORD TOOL ======")
    print("1. Check Password Strength")
    print("2. Generate Password")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        pwd = input("Enter password: ")
        check_strength(pwd)

    elif choice == "2":
        try:
            length = int(input("Enter password length: "))
            generate_password(length)
        except ValueError:
            print(" Enter a valid number")

    elif choice == "3":
        print("Goodbye ")
        break

    else:
        print("❌ Invalid choice")