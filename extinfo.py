# @ By Cristo Emiliano Hernandez Daria
#
# Obtenga información detallada sobre una extensión individual o múltiples extensiones. 
# Por ejemplo, los desarrolladores pueden consultar la configuración avanzada de una extensión. 
# Cuando haya varias solicitudes, sepárelas con comas
# help : https://help.yeastar.com/en/s-series-developer/api/api_query_extension_settings.html
'''
POST /api/v1.1.0/extension/query?token=277ac400357b509b4a587ff2157f7ad5 HTTP/1.1
Content-Type:application/json; charset=utf-8
Host: 192.168.5.150
{
    "extid":"1000"
}
'''
import requests
import json
import urllib3
import os.path
import os, sys

os.getcwd()
urllib3.disable_warnings()

cadena_json = ""
extension = ""

def extinf(extdata): # Recoge información de una extensión y lo envia a un json en formato json
    import data
    from take_token import _getoken_
    token = _getoken_() #Token sera igual a lo que me devuelva la funcion _gettoken_ de take_token.py
    
    url = "https://" + data.host + ":8088/api/v1.1.0/extension/query?&token=" + token
    payload="{ \"extid\":\"" + extdata + "\"}"
    headers ={
        'host': data.host,
         }
    # Se almacena el la variable el resultado del POST
    list = requests.request("POST", url, headers=headers, data=payload, verify=False)
    cadena_json = list.json()
    
    ## Almacenamos la respuesta en un archivo json llamado 'extinfo.josn' 
    with open(data.ruta_json_extinfo, 'w') as json_file:
        json.dump(cadena_json, json_file)
    
    return cadena_json



