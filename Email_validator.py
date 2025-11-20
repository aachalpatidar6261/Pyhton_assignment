def email_validates(email):
    if email[-10:] == "@gmail.com":
        return "Valid Email"
    else:
        return "Not valid"

email = "Example123@gmail.com"
print(email_validates(email))