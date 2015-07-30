from bottle import Bottle, run, static_file, request
import os, bottle, shutil, time, tcs_bottle_config, telescope, camera

app = Bottle()

@app.route('/getposition')
def getposition():
	return telescope.get_RA_DEC('percent_of_rev')

@app.route('/listconfig')
def list_config():	
	return gphoto.get_list(['--list-config'])		
	
@app.route('/getconfig')
def get_config():	
	querystring = request.query.configkey.strip()
	return gphoto.execute(['--get-config', querystring])		
	
@app.route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root=tcs_bottle_config.config['bottle_staticfilepath'], mimetype="text/html")

@app.route('/listsummary')
def summary():
	return gphoto.get_list(['--summary'])		

@app.route('/captureimage')
def capture_image():
	
	timestring = 'gphoto_' + time.strftime('%Y%m%d_%H%M%S') + '.jpg'
	capture = gphoto.execute(['--set-config', '/main/actions/autofocusdrive=1', '--capture-image-and-download'])	
	if "capt0000.jpg" in capture:
		# move the image to the static folder
		shutil.copy('capt0000.jpg', 'static/' + timestring)
		os.remove('capt0000.jpg')
		return timestring
		
	return "false"
	
@app.route('/capturepreview')
def capture_preview():
	capture = gphoto.execute(['--set-config', '/main/actions/autofocusdrive=1', '--capture-preview'])

@app.route('/listabilities')
def list_abilities():
	return gphoto.get_list(['--abilities'])	
	
@app.route('/storageinfo')
def storage_info():
	#return gphoto.execute(['--storage-info'])
	return 'Storage info!'

@app.route('/resetconnection')
def reset_camera_connection():	
	is_usb_reset = gphoto.resetusb()
	if is_usb_reset:
		return "Camera connection " + gphoto.global_usb_port + " has been reset"

	return "Error resetting camera connection. Check connection."


			

bottle.debug(tcs_bottle_config.config['bottle_debug'])
run(app, host=tcs_bottle_config.config['bottle_ip'], port=tcs_bottle_config.config['bottle_port'], reloader=tcs_bottle_config.config['bottle_reloader'])