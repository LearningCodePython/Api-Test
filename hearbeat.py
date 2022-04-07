# @ By Cristo Emiliano Hernandez Daria
#
'''
POST /api/v1.1.0/heartbeat?token=277ac400357b509b4a587ff2157f7ad5 HTTP/1.1
Content-Type:application/json; charset=utf-8
Host: 192.168.5.150
{
"url": "192.168.5.122:8260/report",urlflag: "1"
}
'''

import requests
import urllib3
import take_token
import data

urllib3.disable_warnings()

def heartbreat(): # se declara la funcion heartbreat
  url = "https://" + data.host + ":8088/api/v1.1.0/heartbeat?token=" + take_token.token
  payload="{ ,\"url\":" + data.ip_server_api  + ",\"urlflag\": \"1\"}"
  headers = {
    'Content-Type': 'text/plain'
  }
  response = requests.request("POST",url, headers=headers, data=payload, verify=False)
  jsonResponse = response.json() 
  # print (jsonResponse)
heartbreat()