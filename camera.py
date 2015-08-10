#!/usr/bin/python
# -*- coding: UTF-8 -*-

import subprocess, tcs_bottle_config

global_usb_port = None

def list_config():
	command = ['--list-config']
	execute_response = _execute_command(command)	
	return execute_response

def get_config(param):	
	command = ['sudo', 'gphoto2', '--get-config', param]
	execute_response = subprocess.check_output(command)
	return execute_response

def get_current_image_config():
	response = _verify_camera()
	if response == "Camera not found":
		return 'Error: ' + response + '. Check the camera connections and make sure is On'

	current = 'Image Size: ' + get_config('imagesize').split("\n")[2].split(" ")[1]
	current += '; ISO Speed: ' + get_config('iso').split("\n")[2].split(" ")[1]
	current += '; WhiteBalance: ' + get_config('whitebalance').split("\n")[2].split(" ")[1]
	return current

def get_current_capture_config():
	response = _verify_camera()
	if response == "Camera not found":
		return 'Error: ' + response + '. Check the camera connections and make sure is On'

	current = 'Exposure Compensation: ' + get_config('exposurecompensation').split("\n")[2].split(" ")[1]
	current += '; Flash Mode: ' + get_config('flashmode').split("\n")[2].split(" ")[1]
	current += '; F-Number: ' + get_config('f-number').split("\n")[2].split(" ")[1]
	current += '; Image Quality: ' + get_config('imagequality').split("\n")[2].split(" ")[1]
	current += '; Focus Mode: ' + get_config('focusmode').split("\n")[2].split(" ")[1]
	current += '; Exposure Program: ' + get_config('expprogram').split("\n")[2].split(" ")[1]
	current += '; Still Capture Mode: ' + get_config('capturemode').split("\n")[2].split(" ")[1]
	current += '; Focus Metering Mode: ' + get_config('focusmetermode').split("\n")[2].split(" ")[1]
	current += '; Exposure Metering Mode: ' + get_config('exposuremetermode').split("\n")[2].split(" ")[1]
	current += '; Shutter Speed: ' + get_config('shutterspeed').split("\n")[2].split(" ")[1]
	return current

def capture_sequence(frames, interval):
	response = _verify_camera()
	if response == "Camera not found":
		return 'Error: ' + response + '. Check the camera connections and make sure is On'

	command = ['--capture-image', '-F', frames, '-I', interval]
	execute_response = _execute_command(command)
	return execute_response

def set_config(param, value):
	response = _verify_camera()
	if response == "Camera not found":
		return 'Error: ' + response + '. Check the camera connections and make sure is On'

	param_value = param + '=' + value
	command = ['--set-config', param_value]
	execute_response = _execute_command(command)
	return execute_response

#El nombre de la imagen viene con extensión
def capture_image_and_download(name):
	command = ['--capture_image_and_download', '--filename', name]
	execute_response = _execute_command(command)
	return execute_response	

'''
def capture_preview():
	command = 	
'''

def _execute_command(command):
	#response = _verify_camera()
	gphoto_command = ['sudo', 'gphoto2'] + command
	gphoto_response = subprocess.check_call(gphoto_command)
	return gphoto_response

def execute(command):
	
	if _detectcamera() == False:
		return "Camera not found"
	
	resetusb()	
	gphotocommand = ['sudo', 'gphoto2'] + command
	gphoto_response = subprocess.check_output(gphotocommand)
	resetusb()
	
	return gphoto_response

def _verify_camera():
	if _detectcamera() == False:
		return "Camera not found"

	resetusb()

def _detectcamera():
	gphoto_detect = subprocess.check_output(['sudo', 'gphoto2', '--auto-detect'])
	
	if gphoto_detect == None:
		return False
		
	usb_device = gphoto_detect.split(":")
	if len(usb_device) < 2:
		return False
	else:
		usb_device = usb_device[1].strip().replace(",","/")
		global global_usb_port
		global_usb_port = usb_device
		return True		

def resetusb():	
	if global_usb_port != None:
		subprocess.Popen(['sudo', tcs_bottle_config.config['usbresetpath'], '/dev/bus/usb/' + global_usb_port])
		return True
	else:
		return False