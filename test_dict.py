import data
import json
from pbxinfo import uptime, extensionstatus

f = open(data.ruta_json_pbxinfo, "r") #cargo el fichero json

val1 = f.read()

jsondecode = json.loads(val1) #decodifico el fichero a formato json

val2 = (jsondecode['deviceinfo']) # Almaceno en la variable val2 el diccionarion deviceinfo

print (val2["uptime"])
print (val2["extensionstatus"])

print (uptime)
print (extensionstatus)