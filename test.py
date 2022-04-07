'''
from system import _pbxinfo_, cadena_json# Importo los datos de la app
infosystem = _pbxinfo_() #Ejecuto la función y la almaceno en una variable
deviceinfo = infosystem['deviceinfo']
sn = deviceinfo['sn']
print (sn)
'''
import requests
import json
import urllib3
import os.path
import os, sys
import data

os.getcwd()
urllib3.disable_warnings()

cadena_json = ""

def _extlist_():
    
    from take_token import _getoken_
    token = _getoken_() #Token sera igual a lo que me devuelva la funcion _gettoken_ de take_token.py
    
    #Variables locales
    url = "https://" + data.host + ":8088/api/v1.1.0/extensionlist/query?&token=" + token
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        }

    # Se almacena el la variable el resultado del POST
    list = requests.request("POST", url, headers=headers, data=payload, verify=False)
    global cadena_json
    cadena_json = list.json() #esto es un diccionario
    
    ## Almacenamos la respuesta en un archivo json llamado 'extlist.josn' 
    with open(data.ruta_json_extlist, 'w') as json_file:
        json.dump(cadena_json, json_file)
_extlist_()

no_register = 0
def _unavailable_ ():
    f = open(data.ruta_json_extlist, "r")
    contenido = f.read()                        # Se abre el fichero en modo lectura
    jsondecode = json.loads(contenido)          # Se codifica el contenido de 'contenido' y se almacena en 'jsondecode'                  
    lista1 = (jsondecode["extlist"])            # de la variable jsondecode de extrae la clave 'extlist' y se almacena en lista
    list = []
    for i in (lista1):
        if (i["status"] == "Unavailable"):
            global no_register
            no_register = no_register + 1
            list.append(i)
    return list
_unavailable_()

archivo = open("contador1.txt","w")
a = no_register
archivo.write(str((a)))
archivo.close()

def _leer_():
    total = open("contador1.txt","r")
    valor = total.readline()
    
    print (valor)
_leer_()