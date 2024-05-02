"""
Check the strength of a password, based on the following:
- It must contain at least 1 lowercase characters.
- It must contain at least 1 uppercase characters.
- It must contain at least 1 non-word characters.
- It must contain at least 1 digits.
- It must contain at least 8 characters.
"""
import re


def check_pwd_strenght(pwd):
    # Execute the following validation:
    # (?=.*[a-z])              It must contain at least 1 lowercase characters.     # noqa
    # (?=.*[A-Z])              It must contain at least 1 uppercase characters.     # noqa
    # (?=.*\W)                 It must contain at least 1 non-word characters.      # noqa
    # (?:.*\d)                 It must contain at least 1 digits.                   # noqa
    # (?=.){8,}                It must contain at least 8 characters.               # noqa
    pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\W)(?:.*\d)(?=.){8,}'  # noqa
    if re.search(pattern, pwd):
        return True
    else:
        return False


if __name__ == '__main__':
    password_to_check = [
        "SecureP@ssw0rd", "securepassword",
        "SecurePassword", "SecurePassw0rd",
        "Secur3", "S!cur3"
    ]

    for pwd in password_to_check:
        if check_pwd_strenght(pwd):
            print(f"{pwd} >> Password is strong!")
        else:
            print(f"{pwd} >> Password does not meet the criteria.")
