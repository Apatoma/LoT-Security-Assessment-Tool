def sanitize_input(user_input):
    # Simple sanitation example to prevent command injection
    return user_input.replace(';', '').replace('&', '')
