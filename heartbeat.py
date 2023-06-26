
import requests
from requests.models import Response
import urllib3
import data

urllib3.disable_warnings()

def heartbeat (): # Función que captura el token para almacenarlo en la variable toke.
    #£from take_token import _getoken_
    #token = _getoken_() #Token sera igual a lo que me devuelva la funcion _gettoken_ de take_token.py
    url = "https://" + data.host + ":8088/api/v1.1.0/heartbeat?&token=22a3730d086a58dc686d0caa36aa50e5"

    payload="{ \"ipaddr\":\"192.168.0.114\",\"port\": \"8260\"}"
    #payload="{ \"ipaddr\":\"192.168.0.114\",\"port\": \"8260\"}"
    headers = {
        'Content-Type': 'text/plain'
    }
    r = requests.post(url, headers=headers, data=payload, verify=False)
    jsonResponse = r.json()
    #token_ = (jsonResponse["token"]) #Selecciona al valor de la clave "token"
    print (jsonResponse)

heartbeat()