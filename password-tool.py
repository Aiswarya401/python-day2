import random
import string

def check_strength(password):
    length = len(password)

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if length >= 8 and score == 4:
        return "🔥 Strong"
    elif length >= 6 and score >= 3:
        return "🙂 Medium"
    else:
        return "❌ Weak"

def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(all_chars) for _ in range(length))

while True:
    print("\n1. Check Password Strength")
    print("2. Generate Password")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        pwd = input("Enter password: ")
        print("Strength:", check_strength(pwd))

    elif choice == "2":
        length = int(input("Enter length: "))
        print("Generated:", generate_password(length))

    elif choice == "3":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")