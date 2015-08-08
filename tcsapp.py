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

###################################################
############# TELESCOPE ###########################
###################################################

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

@app.route('/gettrackingmode', method='POST')
def get_trackingmode():
    response = telescope.get_tracking_mode()
    print response
    return response

@app.route('/settrackingmode', method='POST')
def set_trackingmode():
    mode = int(request.forms.get('trackingmode'))
    response = telescope.set_tracking_mode(mode)
    print response
    return response

@app.route('/slewing', method='POST')
def slewing():
    rate_type = request.forms.get('ratetype')
    direction = request.forms.get('direction')
    rate = int(request.forms.get('rate'))

    if rate_type == 'var':
        response = telescope.slew_var_rate(direction, rate)
    else:
        response = telescope.slew_fixed_rate(direction, rate)

    print response
    return response

@app.route('/getlocation', method='POST')
def getlocation():
    response = telescope.get_location()
    print response
    return response
            
@app.route('/setlocation', method='POST')
def setlocation():
    a = int(request.forms.get('a'))
    b = int(request.forms.get('b'))
    c = int(request.forms.get('c'))
    d = int(request.forms.get('d'))
    e = int(request.forms.get('e'))
    f = int(request.forms.get('f'))
    g = int(request.forms.get('g'))
    h = int(request.forms.get('h'))
    response = telescope.set_location(a, b, c, d, e, f, g, h)
    print response
    return response

@app.route('/gettime', method='POST')
def gettime():
    response = telescope.get_time()
    print response
    return response

@app.route('/settime', method='POST')
def settime():
    q = int(request.forms.get('q'))
    r = int(request.forms.get('r'))
    s = int(request.forms.get('s'))
    t = int(request.forms.get('t'))
    u = int(request.forms.get('u'))
    v = int(request.forms.get('v'))
    w = int(request.forms.get('w'))
    x = int(request.forms.get('x'))
    response = telescope.set_time(q,r,s,t,u,v,w,x)
    print response
    return response

@app.route('/gpscheck', method='POST')
def gps_check():
    response = telescope.is_gps_linked()
    print response
    return response

@app.route('/gpsgetlatitude', method='POST')
def gps_getlatitude():
    response = telescope.gps_get_latitude()
    print response
    return response

@app.route('/gpsgetlongitude', method='POST')
def gps_getlongitude():
    response = telescope.gps_get_longitude()
    print response
    return response

@app.route('/gpsgetdate', method='POST')
def gps_getdate():
    response = telescope.gps_get_date()
    print response
    return response

@app.route('/gpsgettime', method='POST')
def gps_gettime():
    response = telescope.gps_get_time()
    print response
    return response

@app.route('/rtcgetdate', method='POST')
def rtc_getdate():
    response = telescope.rtc_get_date()
    print response
    return response

@app.route('/rtcgettime', method='POST')
def rtc_gettime():
    response = telescope.rtc_get_time()
    print response
    return response

@app.route('/rtcsetdate', method='POST')
def rtc_setdate():
    response = telescope.rtc_set_date()
    print response
    return response

@app.route('/rtcsettime', method='POST')
def rtc_settime():
    response = telescope.rtc_set_time()
    print response
    return response

@app.route('/version', method='POST')
def get_version():
    response = telescope.get_version()
    print response
    return response

@app.route('/deviceversion', method='POST')
def get_deviceversion():
    response = telescope.get_device_version()
    print response
    return response

@app.route('/model', method='POST')
def get_model():
    response = telescope.get_model()
    print response
    return response

###################################################
############# CAMERA ##############################
###################################################
@app.route('/generalsettings', method='POST')
def set_generalsettings():
    param = request.forms.get('parameter')
    value = request.forms.get('value')
    response = camera.set_config(param, value)
    print response
    return response

@app.route('/actualgeneralsettings', method='POST')
def get_generalsettings():
    response = camera.get_actual_general_config()
    print response
    return response

@app.route('/imagesettings', method='POST')
def set_imagesettings():
    param = request.forms.get('parameter')
    value = request.forms.get('value')
    response = camera.set_config(param, value)
    print response
    return response

@app.route('/actualimagesettings', method='POST')
def get_imagesettings():
    response = camera.get_actual_image_config()
    print response
    return response

@app.route('/capturesettings', method='POST')
def set_capturesettings():
    param = request.forms.get('parameter')
    value = request.forms.get('value')
    response = camera.set_config(param, value)
    print response
    return response

@app.route('/actualcapturesettings', method='POST')
def get_capturesettings():
    response = camera.get_actual_capture_config()
    print response
    return response



bottle.debug(tcs_bottle_config.config['bottle_debug'])
run(app, host=tcs_bottle_config.config['bottle_ip'], port=tcs_bottle_config.config['bottle_port'], reloader=tcs_bottle_config.config['bottle_reloader'])