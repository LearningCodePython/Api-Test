# @ By Cristo Emiliano Hernandez Darias.
#
#Consultar la configuración básica y la configuración DOD de una troncal SIP,
# Require 'trunkname' que se pasa como un str en el valor de la función
# múltiples troncales SIP o todas las troncales SIP.
'''
POST /api/v1.1.0/siptrunk/query?token=277ac400357b509b4a587ff2157f7ad5 HTTP/1.1
Content-Type:application/json; charset=utf-8
Host: 192.168.5.150

{
    "trunkname": "SIP"
}
'''
import requests
import json
import urllib3
import os.path

os.getcwd()
urllib3.disable_warnings()

import data
import take_token

def _siptrkinf_(name): # Informacion de un SIP troncal en concreto
    url = "https://" + data.host + ":8088/api/v1.1.0/siptrunk/query?&token=" + take_token.token
    payload="{\"trunkname\":\"" + name + "\"}"
    headers ={

        'host': data.host,
         }
    # Se almacena el la variable el resultado del POST
    list = requests.request("POST", url, headers=headers, data=payload, verify=False)
    cadena_json = list.json()

    ## Almacenamos la respuesta en un archivo json llamado 'siptrkinfo.josn' 
    with open(data.ruta_json_siptrkinfo, 'w') as json_file:
        json.dump(cadena_json, json_file)


# El valor de extdata debe ser un str relacionado con el nombre del troncal SIP, por ejemplo "LCR-Trunk", 
# esto nos creará un archivo *.json con la informacion de la extensión "LCR-Trunk".

_siptrkinf_("LCR-Trunk")