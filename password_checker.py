import re

def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 20
    else:
        feedback.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 20
    else:
        feedback.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 20
    else:
        feedback.append("Add lowercase letters")

    if re.search(r"\d", password):
        score += 20
    else:
        feedback.append("Add numbers")

    if re.search(r"[!@#$%^&*]", password):
        score += 20
    else:
        feedback.append("Add special symbols")

    if score < 40:
        strength = "Weak"
    elif score < 80:
        strength = "Medium"
    else:
        strength = "Strong"

    return score, strength, feedback