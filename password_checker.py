import re

def password_strength(password):
    length = len(password)
    score = 0
    
    # Criteria weights
    length_weight = 2
    uppercase_weight = 2
    lowercase_weight = 2
    number_weight = 2
    special_char_weight = 3
    
    # Check length
    if length >= 8:
        score += length_weight
    else:
        return "Weak password: Too short"
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += uppercase_weight
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += lowercase_weight
    
    # Check for numbers
    if re.search(r'\d', password):
        score += number_weight
    
    # Check for special characters
    if re.search(r'[!@#$%^&*()-+=]', password):
        score += special_char_weight
    
    # Determine strength
    if score >= 10:
        return "Strong password"
    elif score >= 6:
        return "Moderate password"
    else:
        return "Weak password: lack of complexity"

# Example usage
password = input("Enter your password: ")
strength = password_strength(password)
print("Password strength:", strength)
