# @ By Cristo Emiliano Hernandez Daria
#
import hashlib

contraseña = input("¿Contraseña?")
h = hashlib.new("md5",b,contraseña)

# h = hashlib.new("md5",b"Emilio54")

print(h.hexdigest())
