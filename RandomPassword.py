import random
import string

password_type = input("type-(str, int, mix): >>> ")
password_len = int(input("len: >>> "))
password_quantity = int(input("quantity: >>> "))

if password_type not in ['str', 'int', 'mix']:
    print("error")
else:
    def password_str(_len, quantity):
        passwords = []
        for i in range(quantity):
            pas = [random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(_len)]
            passwords.append("".join(pas))
        return passwords


    def password_int(_len, quantity):
        passwords = []
        for i in range(quantity):
            pas = [random.choice(string.digits) for i in range(_len)]
            passwords.append("".join(pas))
        return passwords

    def password_mix(_len, quantity):
        passwords = []
        for i in range(quantity):
            pas = [random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase + string.digits) for i in range(_len)]
            passwords.append("".join(pas))
        return passwords

    if password_type == 'int':
        print(password_int(password_len, password_quantity))
    elif password_type == "str":
        print(password_str(password_len, password_quantity))
    else:
        print(password_mix(password_len, password_quantity))