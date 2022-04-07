# @ By Cristo Emiliano Hernandez Daria
#
# Configure los ajustes de una extensión individual, 
# como número de extensión, nombre, registros simultáneos, dirección de correo electrónico, 
# extensión de movilidad, etc.
# Funcion que cuenta y almacena en un txt el numero de extensones no registradas.
# help : https://help.yeastar.com/en/s-series-developer/api/api_modify_an_extension.html
# Ejemplo de request.
'''
POST /api/v1.1.0/extension/update?token=277ac400357b509b4a587ff2157f7ad5 HTTP/1.1
Content-Type:application/json; charset=utf-8
Host: 192.168.5.150
{
    "extid": "1002",
    "username": "Amy"
}
'''
# Para que estas funciónes se ejecuten correctamente debemos pasarle los valores, número de extension, valor.
# ayuda en : https://help.yeastar.com/en/s-series-developer/api/api_modify_an_extension.html

import requests
from requests.api import request
import urllib3
import os.path
import json


os.getcwd()
urllib3.disable_warnings()

import data

# Para que esta función se ejecute correctamente debemos pasarle dos valores, número de extension, valor.
# ayuda en : https://help.yeastar.com/en/s-series-developer/api/api_modify_an_extension.html

def _ext_dnd_(extnum, value): #Avtiva o desactiva el DND con el valor de la ext y on/off.
    
    from take_token import _getoken_
    token = _getoken_() #Token sera igual a lo que me devuelva la funcion _gettoken_ de take_token.py

    url = "https://" + data.host + ":8088/api/v1.1.0/extension/update?&token=" + token
    payload="{ \"extid\":\"" + extnum + "\", \"dnd\":\"" + value + "\"}"
    headers ={
        'host': data.host,
         }
    # Se almacena el la variable el resultado del POST
    list = requests.request("POST", url, headers=headers, data=payload, verify=False)
    # cadena_json = list.json()# 

def _ext_name_(extnum, value): #Cambie el campo 'Caller ID name' o nombre de extesnión.
    
    from take_token import _getoken_
    token = _getoken_() #Token sera igual a lo que me devuelva la funcion _gettoken_ de take_token.py

    url = "https://" + data.host + ":8088/api/v1.1.0/extension/update?&token=" + token
    payload="{ \"extid\":\"" + extnum + "\", \"username\":\"" + value + "\"}"
    headers ={
        'host': data.host,
         }
    # Se almacena el la variable el resultado del POST
    list = requests.request("POST", url, headers=headers, data=payload, verify=False)

def _ext_email_(extnum, value): # Cambia o asigna un correo electronico a la extensión.
    
    from take_token import _getoken_
    token = _getoken_() #Token sera igual a lo que me devuelva la funcion _gettoken_ de take_token.py

    url = "https://" + data.host + ":8088/api/v1.1.0/extension/update?&token=" + token
    payload="{ \"extid\":\"" + extnum + "\", \"email\":\"" + value + "\"}"
    headers ={
        'host': data.host,
         }
    # Se almacena el la variable 'list' el resultado del POST
    list = requests.request("POST", url, headers=headers, data=payload, verify=False)

def _ext_movil_(extnum, value): # Cambia o asigna un número de movil a la extension.
    
    from take_token import _getoken_
    token = _getoken_() #Token sera igual a lo que me devuelva la funcion _gettoken_ de take_token.py

    url = "https://" + data.host + ":8088/api/v1.1.0/extension/update?&token=" + token
    payload="{ \"extid\":\"" + extnum + "\", \"mobile\":\"" + value + "\"}"
    headers ={
        'host': data.host,
         }
    # Se almacena el la variable 'list' el resultado del POST
    list = requests.request("POST", url, headers=headers, data=payload, verify=False)

## Esta parte intentará extrael el número de extensiones no registradas
## Ahora cargamos el contenido del achivo extlist.josn en la variable content 

no_register = 0 #Asignacion del valor inicial 0 a la variable no_register.

def reset_value(): #Función que al ejecutarla reinicia el valor de la variable globarl 'no_register' a 0
    global no_register
    no_register = 0

def _unavailable_ (): #Función que extrae la cantidad de extensiones no regitradas y las almacena en una lista
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

# Leer un arcivo TXT con el valor de las extensiones no registradas en formato STR desde un TXT
_unavailable_()

archivo = open("contador1.txt","w")     # abro un archivo llamado contador1.txt para escribir en el
a = no_register     # le asigno el valor de no_register a la variable 'a' -Creo que se puede simplificar
archivo.write(str((a)))     #Escribo en el fichero el valor de a que a su ves es el valor de no_register
archivo.close()     #cierro el fichero .txt

def _leer_(): #Creo la función _leer_() para consultar el valor de extensiones no registradas
    total = open("contador1.txt","r")
    valor = total.readline()
    print (valor)
_leer_()  


#Ejemplo de como interactuar con la funciones de este programa.

# _ext_dnd_("800","off")
# _ext_name_("800","Pruebas")
# _ext_email_("800","tucorreo@gmail.com")
# _ext_movil_("800","646192190")