# @ By Cristo Emiliano Hernandez Daria
#
import hashlib
import sys
entrada = sys.argv[-1]

def newhash(valor):
    p_encode= valor.encode()
    h = hashlib.new("md5", p_encode)
    password = (h.hexdigest())
    print (password)
newhash(entrada)
