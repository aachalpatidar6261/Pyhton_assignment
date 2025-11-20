def password_checker(password):
    length = len(password) >= 8 
    upper = any(ch.isupper() for ch in password)
    lower = any(ch.islower() for ch in password)
    digit = any(ch.isdigit() for ch in password)
    special = any(ch in "!@#$%^&*(){}[]-=_+:;?/|\.,<>" for ch in password)

    score = sum([length, upper, lower, digit, special])
    if score == 5:
        print("Strong Password!")
    elif score>=3:
        print("Moderate Password!")
    else:
        print("Weak Password!")


user_password = input("Enter Password : ")
password_checker(user_password)