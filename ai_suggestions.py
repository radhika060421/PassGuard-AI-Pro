def generate_suggestion(password):

    suggestions = []

    if len(password) < 8:
        suggestions.append(
            "Increase password length"
        )

    if password.islower():
        suggestions.append(
            "Add uppercase letters"
        )

    if password.isalpha():
        suggestions.append(
            "Add numbers and symbols"
        )

    return suggestions