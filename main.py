import random
elements = "+-/$%#?¡abcdefghijklmnpqrstuvyzABCDEFGHIJLMNPOQRSTUVWYZ12345678910
pass_length = int(input("introduzca a la longitud de la contraseña:"))
password= ""
for i in range(pass_length):
    password += random.choice(elements)
    print(password) 
