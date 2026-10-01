import numpy as np

msg = "Roll a dice!"
print(msg)

print(np.random.randint(1,9))

# Solicita al usuario que ingrese un número.
num = int(input("Ingrese un número: "))

# Utiliza un bucle for para iterar desde 1 hasta 10 e imprime cada multiplicación.
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")