# @ By Cristo Emiliano Hernandez Daria
#
import requests
import urllib3
import os.path
import os
import data

os.getcwd()
urllib3.disable_warnings()

random_ = 0

def crd_random(): #Captura la clave random y la almacena en la variable random_
    
    from take_token import _getoken_
    token = _getoken_() #Token sera igual a lo que me devuelva la funcion _gettoken_ de take_token.py
    
    url = "https://" + data.host + ":8088/api/v1.1.0/cdr/get_random?&token=" + token
    payload="{\"extid\": \"all\", \"starttime\" : \"2021-12-09 00:00:00\", \"endtime\" : \"2021-12-09 23:59:59\" }"
    headers ={
                'Content-Type': 'application/json',
             }
         
    # Se almacena el la variable list el resultado del POST

    list = requests.request("POST", url, headers=headers, data=payload, verify=False)
    cadena_json = list.json()       # Se codifica el rosultado en formato Json
    clave = (cadena_json["random"]) #Selecciona al valor de la clave "random"
    global random_ # Selecciono la variable global random_
    random_ = clave # Le paso el valo de la clave random a la variable 'random_'
    return
crd_random()

print (random_)