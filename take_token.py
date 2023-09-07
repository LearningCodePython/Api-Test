# by : Cristo Emiliano Hernandez Darias 
#
## Repo API_Yeastar in 10.19.19.16/BonoboGit
## Nueva rama para hacer pruebas con la central de Guayarmina 10.102.0.10

## take_toke.py se concecta con la central y almacena en la variable tocken el valor de token necesario
## para posteriormente hacer el POST a la central, necesario para interectuar con la API de la Yeastar

import requests
from requests.models import Response
import urllib3
import data

urllib3.disable_warnings()

def _getoken_ (): # Función que captura el token para almacenarlo en la variable toke.
  url = "https://" + data.host + ":8088/api/v1.1.0/login"
  payload="{ \"username\":" + data.api_user + ",\"password\":" + data.api_pass + ",\"port\": \"8260\" }"
  headers = {
    'Content-Type': 'text/plain'
  }
  r = requests.post(url, headers=headers, data=payload, verify=False)
  jsonResponse = r.json()
  token = (jsonResponse["token"]) #Selecciona al valor de la clave "token"cd 
  return token
llave = _getoken_()

