import random
passwordlength = int(input("enter the length of the required password"))
Specialsymbols="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
required_password = "".join(random.sample(Specialsymbols,passwordlength ))
print(required_password)