import random, string

caracteres = string.ascii_letters
numeros = string.digits
puntuacion = string.punctuation
# password = ""

n_carac = int(input("Cuantas letras quieres? "))
n_numeros = int(input("Cuantos números quieres? "))
n_pun = int(input("Cuantos signos de puntuación quieres? "))

# for i in range(n_carac + 1):
#     password += random.choice(caracteres)
# for i in range(1, n_numeros + 1):
#     password += random.choice(numeros)
# for i in range(1, n_pun + 1):
#     password += random.choice(puntuacion)



#Hard mode
password = []
for i in range(1 + n_carac + 1):
    password.append(random.choice(caracteres))
for i in range(1 + n_numeros + 1):
    password += random.choice(numeros)
for i in range(1 + n_pun + 1):
    password += random.choice(puntuacion)

random.shuffle(password)

password2 = ""
for j in password:
    password2 += j

print(f"Tu contraseña será: {password2}")