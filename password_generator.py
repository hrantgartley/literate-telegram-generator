# Grant Hartley
# 16 July 2023
# A program that asks the end-user for a length of a password
# and it returns a random password based on the length

import secrets
import string


def welcome() -> None:
    print("Welcome to the password generator")


def main():
    welcome()
    grant = "grant"
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars
    pwd_length = int(input("Enter the length of your desired password: "))

    while pwd_length < 8:
        pwd_length = int(input("Enter the length of your desired password: "))

    while True:
        pwd = ""
        for _ in range(pwd_length):
            pwd += "".join(secrets.choice(alphabet))
        if (
            any(char in special_chars for char in pwd)
            and sum(char in digits for char in pwd) >= 2
        ) and (not any(pwd[i] == pwd[i + 1] for i in range(len(pwd) - 1))):
            break
    print(pwd)


main()
