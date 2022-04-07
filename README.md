# Repositorio en GitHub
* Este repositorio lo empiezo desde home_acer.

Programa que intenta dar solución a la necesidad de poder interactuar con las centrales Yeastar, a traves de la función API que tiene la central.

Consta de varios directorios:

# Directorio.

**\/** , almacena todas las aplicaciones en código python.

**/templates** , almacena las paginas web html.

**/json**, almacena las respuesta hechas por la central a las consultas POST.

**/css**, almacena los estilos.

**/contadores**, contiene aquellos ficheros txt usados para almacenar algun valor numérico.

# Python Code.
## data.py

Esta aplicacón es creada para almacenar valores que difieren entre una central (Servidor API) y otra, como la direcion ip, el usuario de la AIP y la contraseña, de esta manera el resto de las aplicaciones seran iguales, indistintamente de la sede a la que se quiera conectar el cliente.

## app.py

Es el aplicación servido web en la que se crean las decoradores de plantillas html esta basada el el framework flask, en este caso he usado flask y jinja por ser mas faciles para el aprendizaje. 

## take_token.py

 Esta aplicacion se conecta a la central y genera un  token que lo almacena an la variable 'token' que luego usaremos en cada una de las solicitudes que le haremos a la central.
    
    import requests
    from requests.models import Response
    import urllib3
    import data
    urllib3.disable_warnings()
    def _getoken_ (): # Función que captura el token para almacenarlo en la variable toke.
        url = "https://" + data.host + ":8088/api/v1.1.0/login"
        payload="{ \"username\":" + data.api_user + ",\"password\":" + data.api_pass+ ",\"port\": \"8260\"}"
        headers = {
            'Content-Type': 'text/plain'
        }
        r = requests.post(url, headers=headers, data=payload, verify=False)
        jsonResponse = r.json()
        token = (jsonResponse["token"]) #Selecciona al valor de la clave "token"
        return token

# Crear alarmas.

Esta parte del app.py deberia debe ser modificada, ya que desde el index.html llamaremos a un formulario llamado alarmas.html que almacenará los datos que necesitemos modificar.

    @app.route('/alarm') # esta web debe ser un formulario que almacene los datos para envir la alarma a la central.
    # @app.route('/alarm', methods=['POST']) 
    def alarmas():
    '''
    from alarm import addalarm
    _extid = request.form['extid'] # Recogemos el datos del Post desde la 'from' de navegacion
    _time = request.form['time'] # Recogemos el datos del Post desde la 'from' de navegacion
    _type = request.form['type'] # Recogemos el datos del Post desde la 'from' de navegacion
    _repeats = request.form['repeats'] # Recogemos el datos del Post desde la 'from' de navegacion
    _interval = request.form['interval'] # Recogemos el datos del Post desde la 'from' de navegacion
    var1 = addalarm(_extid,_time,_type,_repeats,_interval) # Ahora pasamos el valor recogido a la funcion '_extinf_'
    return render_template('alarmas.html', datos = var1[_extid])
    '''
    return render_template('alarmas.html')