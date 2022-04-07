# @ By Cristo Emiliano Hernandez Daria
#
## extlis.py toma informacion de data.py y de take_token.py para construir la petición de una lista de 
## extensiones que las almacena en un fichero llamado /json/extlist.json
## importación de librerias y archivos .py donde se almacenan las variables que necesito

import requests
import json
import urllib3
import os.path
import os
import data

os.getcwd()
urllib3.disable_warnings()

cadena_json = ""

def extlist(): # Genera una lista de todas las extesniones en el sistema y las envia a un json en formato json
    
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
    return