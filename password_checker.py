import re

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"[0-9]", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    score = 5 - sum([length_error, uppercase_error, lowercase_error, digit_error, special_char_error])

    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    print(f"Password Strength: {strength}")
    if length_error:
        print("- Must be at least 8 characters long")
    if uppercase_error:
        print("- Must include at least one uppercase letter")
    if lowercase_error:
        print("- Must include at least one lowercase letter")
    if digit_error:
        print("- Must include at least one number")
    if special_char_error:
        print("- Must include at least one special character")

# Run this
password = input("Enter your password: ")
check_password_strength(password)
