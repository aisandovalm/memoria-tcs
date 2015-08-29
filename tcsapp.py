from bottle import Bottle, run, static_file, request, route, get, response, template
import os, bottle, shutil, time, tcs_bottle_config, camera , telescope

#Logging part
from requestlogger import WSGILogger, ApacheFormatter
from logging.handlers import TimedRotatingFileHandler
import logging

#En tcssystem.log se almacenan todos los eventos de log
logging.basicConfig(filename='static/tcssystem.log', level=logging.DEBUG)

app = Bottle()

@app.hook('after_request')
def enable_cors():
    print "after_request hook"
    logging.debug("after_request hook")
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

@app.route('/')
def root():
    return static_file('index.html', root=tcs_bottle_config.config['bottle_staticfilepath'], mimetype="text/html")

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=tcs_bottle_config.config['bottle_staticfilepath'], mimetype="text/html")

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
    logging.debug(str(response))
    return str(response)

@app.route('/gotoradec', method='POST')
def goto_radec():
    f = request.forms.get('format')
    ra = float(request.forms.get('ra'))
    dec = float(request.forms.get('dec'))
    response = telescope.goto_RA_DEC(ra, dec, f)
    print response
    logging.debug(response)
    return response

@app.route('/gotopreciseradec', method='POST')
def goto_preciseradec():
    f = request.forms.get('format')
    ra = float(request.forms.get('ra'))
    dec = float(request.forms.get('dec'))
    response = telescope.goto_precise_RA_DEC(ra, dec, f)
    print response
    logging.debug(response)
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
    logging.debug(response)
    return response

@app.route('/gotoazmalt', method='POST')
def goto_azmalt():
    f = request.forms.get('format')
    azm = float(request.forms.get('azm'))
    alt = float(request.forms.get('alt'))
    response = telescope.goto_AZM_ALT(azm, alt, f)
    print response
    logging.debug(response)
    return response  

@app.route('/gotopreciseazmalt', method='POST')
def goto_preciseazmalt():
    f = request.forms.get('format')
    azm = float(request.forms.get('azm'))
    alt = float(request.forms.get('alt'))
    response = telescope.goto_precise_AZM_ALT(azm, alt, f)
    print response
    logging.debug(response)
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
    logging.debug(response)
    return response

@app.route('/syncradec', method='POST')
def sync_radec():
    f = request.forms.get('format')
    ra = float(request.forms.get('ra'))
    dec = float(request.forms.get('dec'))
    response = telescope.sync_RA_DEC(ra, dec, f)
    print response
    logging.debug(response)
    return response

@app.route('/syncpreciseradec', method='POST')
def sync_preciseradec():
    f = request.forms.get('format')
    ra = float(request.forms.get('ra'))
    dec = float(request.forms.get('dec'))
    response = telescope.sync_precise_RA_DEC(ra, dec, f)
    print response
    logging.debug(response)
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
    logging.debug(response)
    return response

@app.route('/gettrackingmode')
def get_trackingmode():
    response = telescope.get_tracking_mode()
    print response
    logging.debug(response)
    return response

@app.route('/settrackingmode', method='POST')
def set_trackingmode():
    mode = int(request.forms.get('trackingmode'))
    response = telescope.set_tracking_mode(mode)
    print response
    logging.debug(response)
    return response

@app.route('/slewing', method='POST')
def slewing():
    rate_type = request.forms.get('ratetype')
    direction = request.forms.get('direction')
    sign = request.forms.get('ratesign')
    rate = int(request.forms.get('rate'))

    if rate_type == 'var':
        response = telescope.slew_var_rate(direction, sign, rate)
    else:
        response = telescope.slew_fixed_rate(direction, sign, rate)

    print response
    logging.debug(response)
    return response

@app.route('/stopslewing')
def stopslewing():
    response = telescope.stop_slewing()
    print response
    logging.debug(response)
    return response

@app.route('/getlocation')
def getlocation():
    response = telescope.get_location()
    print response
    logging.debug(response)
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
    logging.debug(response)
    return response

@app.route('/gettime')
def gettime():
    response = telescope.get_time()
    print response
    logging.debug(response)
    return response

@app.route('/settime', method='POST')
def settime():
    q = int(request.forms.get('q'))
    r = int(request.forms.get('r'))
    s = int(request.forms.get('s'))
    t = int(request.forms.get('t'))
    u = int(request.forms.get('u'))
    year = request.forms.get('v')
    v = int(year[2] + year[3])
    w = int(request.forms.get('w'))
    x = int(request.forms.get('x'))
    response = telescope.set_time(q,r,s,t,u,v,w,x)
    print response
    logging.debug(response)
    return response

@app.route('/gpscheck')
def gps_check():
    response = telescope.is_gps_linked()
    print response
    logging.debug(response)
    return response

@app.route('/gpsgetlatitude', method='POST')
def gps_getlatitude():
    format = request.forms.get('format')
    response = telescope.gps_get_latitude(format)
    print response
    logging.debug(response)
    return response

@app.route('/gpsgetlongitude', method='POST')
def gps_getlongitude():
    format = request.forms.get('format')
    response = telescope.gps_get_longitude(format)
    print response
    logging.debug(response)
    return response

@app.route('/gpsgetdate')
def gps_getdate():
    response = telescope.gps_get_date()
    print response
    logging.debug(response)
    return response

@app.route('/gpsgettime')
def gps_gettime():
    response = telescope.gps_get_time()
    print response
    logging.debug(response)
    return response

@app.route('/rtcgetdate')
def rtc_getdate():
    response = telescope.rtc_get_date()
    print response
    logging.debug(response)
    return response

@app.route('/rtcgettime')
def rtc_gettime():
    response = telescope.rtc_get_time()
    print response
    logging.debug(response)
    return response

@app.route('/rtcsetdate', method='POST')
def rtc_setdate():
    day = int(request.forms.get('day'))
    month = int(request.forms.get('month'))
    year = int(request.forms.get('year'))
    response = telescope.rtc_set_date(day, month, year)
    print response
    logging.debug(response)
    return response

@app.route('/rtcsettime', method='POST')
def rtc_settime():
    hours = int(request.forms.get('hours'))
    minutes = int(request.forms.get('minutes'))
    seconds = int(request.forms.get('seconds'))
    response = telescope.rtc_set_time(hours, minutes, seconds)
    print response
    logging.debug(response)
    return response

'''
@app.route('/version', method='POST')
def get_version():
    response = telescope.get_version()
    print response
    logging.debug(response)
    return response

@app.route('/deviceversion', method='POST')
def get_deviceversion():
    device = request.forms.get('device')
    response = telescope.get_device_version(device)
    print response
    logging.debug(response)
    return response

@app.route('/model', method='POST')
def get_model():
    response = telescope.get_model()
    print response
    logging.debug(response)
    return response
'''

###################################################
############# CAMERA ##############################
###################################################
@app.route('/imagesettings', method='POST')
def set_imagesettings():
    param = request.forms.get('imgparameter')
    value = request.forms.get('imgparamvalue')
    response = camera.set_config(param, value)
    print response
    if response == 0:
        logging.debug('Parameter was set correctly, successful operation')
        return 'Parameter was set correctly, successful operation'
    else:
        logging.debug(response)
        return response

@app.route('/currentimagesettings')
def get_imagesettings():
    response = camera.get_current_image_config()
    print response
    logging.debug(response)
    return response

@app.route('/capturesettings', method='POST')
def set_capturesettings():
    param = request.forms.get('captureparameter')
    value = request.forms.get('captureparamvalue')
    response = camera.set_config(param, value)
    print response
    if response == 0:
        logging.debug('Parameter was set correctly, successful operation')
        return 'Parameter was set correctly, successful operation'
    else:
        logging.debug(response)
        return response

@app.route('/currentcapturesettings')
def get_capturesettings():
    response = camera.get_current_capture_config()
    print response
    logging.debug(response)
    return response

@app.route('/imagesequence', method='POST')
def capture_imagesequence():
    frames = request.forms.get('frames')
    interval = request.forms.get('timeinterval')
    if frames == '': #Para prevenir infinitas imagenes
        logging.debug('Error: Invalid number of images. Please try again')
        return 'Error: Invalid number of images. Please try again'
    if interval == '': #Para prevenir infinito tiempo entre imagenes
        logging.debug('Error: Invalid time interval. Please try again')
        return 'Error: Invalid time interval. Please try again'
    response = camera.capture_sequence(frames, interval)
    print response
    if response == 0:
        logging.debug('The sequence has finished, successful operation')
        return 'The sequence has finished, successful operation'
    else:
        logging.debug(response)
        return response

@app.route('/batterylevel')
def get_batterylevel():
    response = camera.get_batterylevel()
    print response
    logging.debug(response)
    return response

@app.route('/capturepreview')
def capturepreview():
    if os.path.isfile('static/preview.jpg'):
        os.remove('static/preview.jpg')

    response = camera.capture_preview()
    
    if response == 'captured':
        shutil.copy('capt0000.jpg', 'static/preview.jpg')
        os.remove('capt0000.jpg')
        return 'preview.jpg'
    else:
        return 'Error'

#En bottleserver.log se almacenan solo los logs correspondientes al servidor (htttp requests)
handlers = [TimedRotatingFileHandler('static/bottleserver.log', 'd', 7),]
app = WSGILogger(app, handlers, ApacheFormatter())


bottle.debug(tcs_bottle_config.config['bottle_debug'])
run(app, host=tcs_bottle_config.config['bottle_ip'], port=tcs_bottle_config.config['bottle_port'], reloader=tcs_bottle_config.config['bottle_reloader'])
