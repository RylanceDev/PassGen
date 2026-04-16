import secrets
import string

def generate_password(length=16, use_symbols=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"

    charset = lower + upper + digits
    if use_symbols:
        charset += symbols

    password = [
        secrets.choice(lower),
        secrets.choice(upper),
        secrets.choice(digits),
    ]

    if use_symbols:
        password.append(secrets.choice(symbols))

    while len(password) < length:
        password.append(secrets.choice(charset))

    secrets.SystemRandom().shuffle(password)
    return "".join(password)