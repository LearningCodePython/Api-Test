# @ By Cristo Emiliano Hernandez Darias.
#
# Consultar la configuración básica de una ruta entrante, 
# varias rutas entrantes o todas las rutas entrantes. Para solicitar todas las rutas entrantes.
# establecer "name" en "all".
'''
POST /api/v1.1.0/inroute/query?token=277ac400357b509b4a587ff2157f7ad5 HTTP/1.1
Content-Type:application/json; charset=utf-8
Host: 192.168.5.150
{
    "name": "Routein" o poner "all"
}
'''
import requests
import json
import urllib3
import os.path
import data

os.getcwd()
urllib3.disable_warnings()

cadena_json = ""

def outrouteinfo(): #Captura información de las rutas de las llamadas salientes

    from take_token import _getoken_
    token = _getoken_() #Token sera igual a lo que me devuelva la funcion _gettoken_ de take_token.py

    url = "https://" + data.host + ":8088/api/v1.1.0/outroute/query?&token=" + token
    payload="{ \"name\":\"all\"}"
    # payload="{ \"name\":\"" + name + "\"}"
    headers ={
        'host': data.host,
         }

    # Se almacena el la variable el resultado del POST
    list = requests.request("POST", url, headers=headers, data=payload, verify=False)
    cadena_json = list.json()

    ## Almacenamos la respuesta en un archivo json llamado 'inrouteinfo.json' 
    with open(data.ruta_json_outrouteinfo, 'w') as json_file:
        json.dump(cadena_json, json_file)
    
    return cadena_json