import re

def check_password_strength(password):
    # Criteria for checking password strength
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    number_criteria = re.search(r'\d', password) is not None
    special_character_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Initialize strength and feedback
    strength = 0
    feedback = []

    # Check each criterion and provide feedback
    if length_criteria:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if lowercase_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if uppercase_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if number_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one number.")

    if special_character_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Determine overall strength
    if strength == 5:
        strength_label = "Very Strong"
    elif strength == 4:
        strength_label = "Strong"
    elif strength == 3:
        strength_label = "Medium"
    elif strength == 2:
        strength_label = "Weak"
    else:
        strength_label = "Very Weak"

    return strength_label, feedback

# Example usage
password = input("Enter a password to check its strength: ")
strength_label, feedback = check_password_strength(password)

print(f"Password strength: {strength_label}")
for comment in feedback:
    print(f"- {comment}")

