#!/usr/bin/python
# -*- coding: UTF-8 -*-

import subprocess, tcs_bottle_config

global_usb_port = None

def list_config():
	command = ['--list-config']
	execute_response = _execute_command(command)	
	return execute_response

def get_config(param):
	command = ['--get-config', param]
	execute_response = _execute_command(command)
	return execute_response

def set_config(param, value):
	command = ['--set-config', param, value]
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
	response = _verify_camera()
	gphoto_command = ['sudo', 'gphoto2'] + command
	gphoto_response = subprocess.check_output(gphoto_command)
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