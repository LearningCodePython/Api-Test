# @ By Cristo Emiliano Hernandez Daria
#
# Consultar información básica como el nombre de la troncal,
# el estado de la troncal, el tipo de troncal, etc. de todas las troncales.
# help https://help.yeastar.com/en/s-series-developer/api/api_query_trunk_list.html
'''
POST /api/v1.1.0/trunklist/query?token=277ac400357b509b4a587ff2157f7ad5 HTTP/1.1
Content-Type:application/json; charset=utf-8
Host: 192.168.5.150
'''
import requests
import json
# import urllib3
import os.path

os.getcwd()
# urllib3.disable_warnings()

import data

cadena_json = ""

def _trklist_(): # Lista de Toncales de la cental.
    
    from take_token import _getoken_
    token = _getoken_() #Token sera igual a lo que me devuelva la funcion _gettoken_ de take_token.py

    url = "https://" + data.host + ":8088/api/v1.1.0/trunklist/query?&token=" + token
    payload={}
    headers ={
        'host': data.host,
         }
    # Se almacena el la variable el resultado del POST
    list = requests.request("POST", url, headers=headers, data=payload, verify=False)
    cadena_json = list.json()
    
    ## Almacenamos la respuesta en un archivo json llamado 'trkinfo.josn' 
    with open(data.ruta_json_trklist, 'w') as json_file:
        json.dump(cadena_json, json_file)
    
    return cadena_json

