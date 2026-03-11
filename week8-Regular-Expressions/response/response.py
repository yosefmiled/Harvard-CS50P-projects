import validators
mail = input("What's your email address? ").strip().lower()
if validators.email(mail) :
    print("Valid")
else :
    print("Invalid")


