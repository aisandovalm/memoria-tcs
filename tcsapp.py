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
def get_position():
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
def goto_radec():
    f = request.forms.get('format')
    ra = float(request.forms.get('ra'))
    dec = float(request.forms.get('dec'))
    response = telescope.goto_RA_DEC(ra, dec, f)
    print response
    return response

@app.route('/gotopreciseradec', method='POST')
def goto_preciseradec():
    f = request.forms.get('format')
    ra = float(request.forms.get('ra'))
    dec = float(request.forms.get('dec'))
    response = telescope.goto_precise_RA_DEC(ra, dec, f)
    print response
    return response

@app.route('/gotoradechdms', method='POST')
def goto_radechdms():
    ra_h = float(request.forms.get('ra_h'))
    ra_m = float(request.forms.get('ra_m'))
    ra_s = float(request.forms.get('ra_s'))
    dec_d = float(request.forms.get('dec_d'))
    dec_m = float(request.forms.get('dec_m'))
    dec_s = float(request.forms.get('dec_s'))
    response = telescope.goto_RA_DEC_hdms(ra_h, ra_m, ra_s, dec_d, dec_m, dec_s)
    print response
    return response

@app.route('/gotoazmalt', method='POST')
def goto_azmalt():
    f = request.forms.get('format')
    azm = float(request.forms.get('azm'))
    alt = float(request.forms.get('alt'))
    response = telescope.goto_AZM_ALT(azm, alt, f)
    print response
    return response  

@app.route('/gotopreciseazmalt', method='POST')
def goto_preciseazmalt():
    f = request.forms.get('format')
    azm = float(request.forms.get('azm'))
    alt = float(request.forms.get('alt'))
    response = telescope.goto_precise_AZM_ALT(azm, alt, f)
    print response
    return response

@app.route('/gotoazmaltdms', method='POST')
def goto_azmaltdms():
    azm_d = float(request.forms.get('azm_d'))
    azm_m = float(request.forms.get('azm_m'))
    azm_s = float(request.forms.get('azm_s'))
    alt_d = float(request.forms.get('alt_d'))
    alt_m = float(request.forms.get('alt_m'))
    alt_s = float(request.forms.get('alt_s'))
    response = telescope.goto_AZM_ALT_dms(azm_d, azm_m, azm_s, alt_d, alt_m, alt_s)
    print response
    return response

@app.route('/syncradec', method='POST')
def sync_radec():
    f = request.forms.get('format')
    ra = float(request.forms.get('ra'))
    dec = float(request.forms.get('dec'))
    response = telescope.sync_RA_DEC(ra, dec, f)
    print response
    return response

@app.route('/syncpreciseradec', method='POST')
def sync_preciseradec():
    f = request.forms.get('format')
    ra = float(request.forms.get('ra'))
    dec = float(request.forms.get('dec'))
    response = telescope.sync_precise_RA_DEC(ra, dec, f)
    print response
    return response

@app.route('/syncradechdms', method='POST')
def sync_radechdms():
    ra_h = float(request.forms.get('ra_h'))
    ra_m = float(request.forms.get('ra_m'))
    ra_s = float(request.forms.get('ra_s'))
    dec_d = float(request.forms.get('dec_d'))
    dec_m = float(request.forms.get('dec_m'))
    dec_s = float(request.forms.get('dec_s'))
    response = telescope.sync_RA_DEC_hdms(ra_h, ra_m, ra_s, dec_d, dec_m, dec_s)
    print response
    return response
			

bottle.debug(tcs_bottle_config.config['bottle_debug'])
run(app, host=tcs_bottle_config.config['bottle_ip'], port=tcs_bottle_config.config['bottle_port'], reloader=tcs_bottle_config.config['bottle_reloader'])