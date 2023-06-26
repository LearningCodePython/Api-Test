import requests
# from requests.api import request
import urllib3
#import os.path

# dados del programa
import data

#os.getcwd()
urllib3.disable_warnings()


def queue_agent(queueid):
    from take_token import _getoken_
    token = _getoken_() #Token sera igual a lo que me devuelva la funcion _gettoken_ de take_token.py

    url = "https://" + data.host + ":8088/api/v1.1.0/queuestatus/query?&token=" + token
    payload="{ \"queueid\":\"" + queueid + "\"}"
    headers ={
        'host': data.host,
         }
    # Se almacena en la variable 'list' el resultado del POST
    list = requests.request("POST", url, headers=headers, data=payload, verify=False)
    cadena_json = list.json()
    status = cadena_json['queues'][0]['queuestatus'][0]['members']
    return status
try:
    for x in (queue_agent("6700")):
        print (x['agent'] + '\t' + x['agentstatus'])
except KeyError:
    print("Ningún agente registrado")
