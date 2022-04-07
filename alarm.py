# @ By Cristo Emiliano Hernandez Daria
#

import requests

def addalarm(extid,time,type,repeats,interval): #Añadir alarma 
    import data
    from take_token import _getoken_
    token = _getoken_() #Token sera igual a lo que me devuelva la funcion _gettoken_ de take_token.py

    ## Usando la IP de la cetal importada de data.host e la variable 'token' creada a partir de la, 
    ## función _gettoken_ constuimos la url para eniviar en el POST.

    url = "https://" + data.host + ":8088/api/v1.1.0/wakeupcall/create?&token=" + token

    payload="{\"extid\":\"" + extid + "\",\"wakeup\":[{\"time\":\"" + time + "\",\"type\":\"" +  type + "\",\"repeats\":\"" + repeats + "\",\"repeatinterval\":\"" + interval + "\"}]}"
    headers ={
        'host': data.host,
         }

    ## Usando la variable addalam_var,
    ## Enviamos la orden con los datos recogidos anteriormente,url paylosd y headres,  a la central.

    addalarm_var = requests.request("POST", url, headers=headers, data=payload, verify=False)
    
    ## La variable jsonresponse almacena la respuesta de la petición POST.

    alarm_jsonresponse = addalarm_var.json()
    
    ## Puntos de control para saber si el programa funciona.
    #print (payload)
    #print (addalarm_var)
    #print (alarm_jsonresponse)

def queryalarm(extid): # Lista de alarmas
    import data
    from take_token import _getoken_
    token = _getoken_() #Token sera igual a lo que me devuelva la funcion _gettoken_ de take_token.py

    ## Usando la IP de la cetal importada de data.host e la variable 'token' creada a partir de la, 
    ## función _gettoken_ constuimos la url para eniviar en el POST.

    url = "https://" + data.host + ":8088/api/v1.1.0/wakeupcall/query?&token=" + token

    payload="{\"extid\":\"" + extid + "\"}"
    headers ={
        'host': data.host,
         }

    ## Usando la variable queryalam_var,
    ## Enviamos la orden con los datos recogidos anteriormente,url paylosd y headres,  a la central.

    queryalarm_var = requests.request("POST", url, headers=headers, data=payload, verify=False)
    
    ## La variable jsonresponse almacena la respuesta de la petición POST.

    query_jsonresponse = queryalarm_var.json()
    
    ## Puntos de control para saber si el programa funciona.
    print (payload)
    print (queryalarm_var)
    print (query_jsonresponse)

def delalarm(extid,time): # Borrar una alarma ya programada
    import data
    from take_token import _getoken_
    token = _getoken_() #Token sera igual a lo que me devuelva la funcion _gettoken_ de take_token.py

    ## Usando la IP de la cetal importada de data.host e la variable 'token' creada a partir de la, 
    ## función _gettoken_ constuimos la url para eniviar en el POST.

    url = "https://" + data.host + ":8088/api/v1.1.0/wakeupcall/delete?&token=" + token

    payload="{\"extid\":\"" + extid + "\",\"time\":\"" + time + "\"}"
    headers ={
        'host': data.host,
         }

    ## Usando la variable queryalam_var,
    ## Enviamos la orden con los datos recogidos anteriormente,url paylosd y headres,  a la central.

    delalarm_var = requests.request("POST", url, headers=headers, data=payload, verify=False)
    
    ## La variable jsonresponse almacena la respuesta de la petición POST.

    del_jsonresponse = delalarm_var.json()
    
    ## Puntos de control para saber si el programa funciona.
    print (payload)
    print (delalarm_var)
    print (del_jsonresponse)

def delallalarm(extid): # Borrar todas las alarmas de una extensión
    import data
    from take_token import _getoken_
    token = _getoken_() #Token sera igual a lo que me devuelva la funcion _gettoken_ de take_token.py

    ## Usando la IP de la cetal importada de data.host e la variable 'token' creada a partir de la, 
    ## función _gettoken_ constuimos la url para eniviar en el POST.

    url = "https://" + data.host + ":8088/api/v1.1.0/wakeupcall/delete?&token=" + token

    payload="{\"extid\":\"" + extid + "\"}"
    headers ={
        'host': data.host,
         }

    ## Usando la variable queryalam_var,
    ## Enviamos la orden con los datos recogidos anteriormente,url paylosd y headres,  a la central.

    delallalarm_var = requests.request("POST", url, headers=headers, data=payload, verify=False)
    
    ## La variable jsonresponse almacena la respuesta de la petición POST.

    delall_jsonresponse = delallalarm_var.json()
    
    ## Puntos de control para saber si el programa funciona.
    print (payload)
    print (delallalarm_var)
    print (delall_jsonresponse)

# ejemplos de llamada a finciones #

#addalarm("800","00:50","onetime","2","5")
#queryalarm("800")
#delalarm("800","00:50")
#delallalarm("800")