# @ By Cristo Emiliano Hernande Darias
#
import requests, json
import urllib3
import os.path
import os
import data

os.getcwd()
urllib3.disable_warnings()



#Variables locales

cadena_json = ""

def pbxinfo(): # Recoge información del sistemas, uptime, n/s, name, etc

    from take_token import _getoken_
    token = _getoken_() #Token sera igual a lo que me devuelva la funcion _gettoken_ de take_token.py

    url = "https://" + data.host + ":8088/api/v1.1.0/deviceinfo/query?&token=" + token
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'host': data.host
        }
    # Se almacena el la variable el resultado del POST
    list = requests.request("POST", url, headers=headers, data=payload, verify=False)
    cadena_json = list.json()

    ## Almacenamos la respuesta en un archivo json llamado 'pbxinfo.josn' 
    with open(data.ruta_json_system, 'w') as json_file:
        json.dump(cadena_json, json_file)
    
    return cadena_json
pbxinfo()
