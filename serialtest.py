#!/usr/bin/python
import serial, io

nexstar = serial.Serial('/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller-if00-port0', baudrate=9600, timeout=1)

def _get_position(command):
	nexstar.write(command)
	response = nexstar.read(18)
	print response

def _goto_command(command):
	nexstar.write(command)
	response = nexstar.read(1)
	print "_goto_command response: " + response
	_validate_command(response)

def _degrees_to_precise(degrees):
	return int(string, 16)/2.**32 * 360

def _validate_command(response):
	assert response == '#', 'Command failed'

def sync_RA_DEC():
	command = ('S34AB, 12CE') 
	nexstar.write(command)
	response = nexstar.read(1)
	print 'sync_RA_DEC response: ' + response


_get_position('e')

#_goto_command('r34BB0500,12BE0500')

sync_RA_DEC()
