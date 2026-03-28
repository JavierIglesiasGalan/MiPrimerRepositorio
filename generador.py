import string
import random

#Solicitamos la longitud de la contraseña
longitud = int(input("Inserta la longitud de la contraseña deseada: "))
#Creamos variable en la cual amacenamos todos los carácteres que queremos que tenga nuestra contraseña
caracteres = string.ascii_letters + string.digits + string.punctuation
#Generamos la contraseña
contrasena = "".join(random.choice(caracteres) for i in range(longitud))
#Imprimimos la contraseña generada
print("Tu contraseña generada es:" + contrasena)