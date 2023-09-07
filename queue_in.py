import requests
# from requests.api import request
import urllib3
#import os.path
import sys
# dados del programa
import data
#os.getcwd()

urllib3.disable_warnings()

# queu_group=input("¿Cual es el numero de cola?")
# extension_numbre=input("¿Cuál es la extenion que quiere salir del grupo?")

def queue_agent(id, extension):
    from take_token import _getoken_
    token = _getoken_() #Token sera igual a lo que me devuelva la funcion _gettoken_ de take_token.py

    #urlin = "https://" + data.host + ":8088/api/v1.1.0/queue/add_dynamicagent?&token=" + token
    #urlout = "https://" + data.host + ":8088/api/v1.1.0/queue/del_dynamicagent?&token=" + token

    url = "https://" + data.host + ":8088/api/v1.1.0/queue/add_dynamicagent?&token=" + token
    payload="{ \"queueid\":\"" + id + "\", \"extid\":\"" + extension + "\"}"
    headers ={
        'host': data.host,
         }
    # Se almacena en la variable 'list' el resultado del POST
    list = requests.request("POST", url, headers=headers, data=payload, verify=False)
    cadena_json = list.json()
    return cadena_json

valor1=(sys.argv[1])
valor2=(sys.argv[2])
queue_agent(valor1,valor2)