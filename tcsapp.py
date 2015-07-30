from bottle import Bottle, run, static_file, request, route, get, response
import os, bottle, shutil, time, tcs_bottle_config, telescope, camera

app = Bottle()

@app.hook('after_request')
def enable_cors():
    print "after_request hook"
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=tcs_bottle_config.config['bottle_staticfilepath'], mimetype="text/html")

@app.route('/ajax', method='POST')
def ajaxtest():
    theText = request.forms.text
    print theText
    if theText:
        return theText
    return "You didn't type anything."

@app.route('/getposition', method='POST')
def getposition():
    c = request.forms.get('coordinates')
    f = request.forms.get('format')
    if c == "RA/DEC":
        response = telescope.get_RA_DEC(f)
    elif c == "precise RA/DEC":
        response = telescope.get_precise_RA_DEC(f)
    elif c == "AZM/ALT":
        response = telescope.get_AZM_ALT(f)
    elif c == "precise AZM/ALT":
        response = telescope.get_precise_AZM_ALT(f)
    print str(response)
    return str(response)

@app.route('/gotoradec', method='POST')
def gotoradec():
    f = request.forms.get('format')
    ra = float(request.forms.get('ra'))
    dec = float(request.forms.get('dec'))
    response = telescope.goto_RA_DEC(ra, dec, f)
    print response
    return response
			

bottle.debug(tcs_bottle_config.config['bottle_debug'])
run(app, host=tcs_bottle_config.config['bottle_ip'], port=tcs_bottle_config.config['bottle_port'], reloader=tcs_bottle_config.config['bottle_reloader'])