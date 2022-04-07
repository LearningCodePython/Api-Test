# @ By Cristo Emiliano Hernandez Daria
#
from flask import Flask, render_template, request
# import extlist


app = Flask(__name__)

@app.route('/')
def index():
    # extlist._extlist_()
    # datosjson = extlist.cadena_json
    return render_template('index.html')
    
@app.route('/todas')
def todas():
    import extlist
    extlist.extlist()
    datosjson = extlist.cadena_json
    return render_template('extlist.html', datos=datosjson['extlist'])


@app.route('/noregister')
def noregister():
    from settingext import _unavailable_, reset_value, no_register
    rst = reset_value() # almaceno en una variable la función que resetea a valor 0 el contador
    lista = _unavailable_() #ejecuto la función para que nos devuelva las extensiones no registradas
    contador = no_register # almaceno en la variable contador el total de las no registradas
    return render_template('noregister.html', datos = lista, cont = contador) # renderizo el tamplate para mostraslo en html

@app.route('/consult', methods=['POST'])
def consult():
    from extinfo import extinf, cadena_json
    _extension = request.form['Extension'] # Recogemos el datos del Post desde la fromulario 'form' de navegacion 'Extensions'
    var1 = extinf(_extension) # Ahora pasamos el valor recogido a la funcion 'extinf'
    return render_template('consult.html', datos = var1['extinfos'])

@app.route('/alarm')
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
    
@app.route('/trunk_list')
def trunk_list():
    from trunklist import _trklist_, cadena_json # Importo los datos de la app
    trklist = _trklist_() # Ejecuto la funcion y la almaceno en la variable trklist
    return render_template('trunk_list.html', datos = trklist['trunklist'])


@app.route('/routein')
def routein():
    from inbandrouteinfo import _inrouteinfo_ # Importo los datos de la app
    routelist = _inrouteinfo_() #Ejecuto la fonción y la almaceno en una variable
    return render_template('routein.html', datos = routelist['inroutes'])

@app.route('/routeout')
def routeout():
    from outbandroute import outrouteinfo # Importo los datos de la app
    routeout = outrouteinfo() #Ejecuto la fonción y la almaceno en una variable
    return render_template('routeout.html', datos = routeout['outroutes'])

@app.route('/system')
def system():
    from system import pbxinfo, cadena_json# Importo los datos de la app
    infosystem = pbxinfo() #Ejecuto la función y la almaceno en una variable
    return render_template('system.html', datos = infosystem['deviceinfo'])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8800, debug=True)
