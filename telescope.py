#!/usr/bin/python
# -*- coding: UTF-8 -*-

import serial, io, math
from serial import SerialException

#Device to connect via serial port
device = '/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller-if00-port0';

#Establish serial connection with telescope. The connection instance is passed to nexstar variable
try:
	nexstar = serial.Serial(device, baudrate=9600, timeout=1)
except SerialException:
	nexstar = None;
	print "Error: Port not found, make sure that the USB/Serial cable is connected to the Raspberry Pi, then restart the app or it will not work properly"

#Variable to check communication
check = 1

#Error messages
msg_error_check = 'Communication problem, check the conections and make sure that the telescope is on. Restart the app'
msg_error_format = 'Error: Invalid format'
msg_error_goto = 'Error: A problem has ocurred with the GOTO command, check the values and try again'

###########################################################################
#Check communication and status functions:							      #
###########################################################################
def echo(x):
	if nexstar != None:
		command = ('K' + chr(x))
		nexstar.write(command)
		response = nexstar.read(2)
		if len(response) == 0:
			return 0
		else:
			return ord(response[0])
	else:
		return 0

def is_alignment_complete():
	nexstar.write('J')
	response = nexstar.read(2)

	align = ord(response[0])
	return True if align == 1 else False

def is_goto_in_progress():
	nexstar.write('L')
	response = nexstar.read(2)
	return True if (int(response[0]) == 1) else False

def cancel_goto():
	nexstar.write('M')
	response = nexstar.read(1)
	return _verify_response(response)	

#Entrega un error si la respuesta del telescopio no es la esperada
def _verify_response(response):
	if response == '#':
		return 'Command received correctly, successful operation'
	else:
		return 'Error: failed operation'


#################################################################################################
#Get Position functions:												                        #
# # format: Specifies format in that the coordinates are required.                               #
#		- 'frac_of_rev': Fracción of a revolution    					                        #	
#		- 'degrees': Decimal degrees											                #
#		- 'H/DMS': Sexagesimal system (Hours:Minutes:Seconds) (Degrees:Arcminutes:Arcosegundos) #
#################################################################################################
def get_RA_DEC(format):
	if echo(check) == check:
		nexstar.write('E')
		response = nexstar.read(10) #Expecting 10 bytes

		ra = _hex_to_frac_of_rev(response[0:4])
		dec = _hex_to_frac_of_rev(response[5:9])

		if format == 'frac_of_rev':
			#return ra, dec
			return "RA: " + str(ra) + ", Dec: " + str(dec)
		elif format == 'degrees':
			#return ra * 360, dec * 360
			return "RA: " + str(ra*360) + ", Dec: " + str(dec*360)
		elif format == 'H/DMS':
			ra_h, ra_m, ra_s  = _dd_to_hms(ra*360)
			dec_d, dec_m, dec_s = _dd_to_dms(dec*360)
			#return ra_h, ra_m, ra_s, dec_d, dec_m, dec_s
			return ("RA: " + str(ra_h) + "h" + str(ra_m) + "m" + str(ra_s) + "s"
				+ " Dec: " + str(dec_d) + "°" + str(dec_m) + "'" + str(dec_s) + '"')
		else:
			return msg_error_format
	else:
		return msg_error_check


def get_precise_RA_DEC(format):
	if echo(check) == check:
		nexstar.write('e')
		response = nexstar.read(18) #Se espera respuesta de 18 bytes

		ra = _hex_precise_to_frac_of_rev(response[0:8])
		dec = _hex_precise_to_frac_of_rev(response[9:17])

		if format == 'frac_of_rev':
			return "RA: " + str(ra) + ", Dec: " + str(dec)
		elif format == 'degrees':
			return "RA: " + str(ra*360) + ", Dec: " + str(dec*360)
		elif format == 'H/DMS':
			ra_h, ra_m, ra_s  = _dd_to_hms(ra*360)
			dec_d, dec_m, dec_s = _dd_to_dms(dec*360)
			return ("RA: " + str(ra_h) + "h" + str(ra_m) + "m" + str(ra_s) + "s"
				+ " Dec: " + str(dec_d) + "°" + str(dec_m) + "'" + str(dec_s) + '"')
		else:
			return msg_error_format
	else:
		return msg_error_check

def get_AZM_ALT(format):
	if echo(check) == check:
		nexstar.write('Z')
		response = nexstar.read(10)

		azm = _hex_to_frac_of_rev(response[0:4])
		alt = _hex_to_frac_of_rev(response[5:9])

		if format == 'frac_of_rev':
			return "Azm: " + str(azm) + ", Alt: " + str(alt)
		elif format == 'degrees':
			return "Azm: " + str(azm*360) + ", Alt: " + str(alt*360)
		elif format == 'H/DMS':
			azm_d, azm_m, azm_s  = _dd_to_dms(azm*360)
			alt_d, alt_m, alt_s = _dd_to_dms(alt*360)
			return ("Azm: " + str(azm_d) + "°" + str(azm_m) + "'" + str(azm_s) + '"'
				+ " Alt: " + str(alt_d) + "°" + str(alt_m) + "'" + str(alt_s) + '"')
		else:
			return msg_error_format
	else:
		return msg_error_check

def get_precise_AZM_ALT(format):
	if echo(check) == check:
		nexstar.write('z')
		response = nexstar.read(18)

		azm = _hex_precise_to_frac_of_rev(response[0:8])
		alt = _hex_precise_to_frac_of_rev(response[9:17])

		if format == 'frac_of_rev':
			return "Azm: " + str(azm) + ", Alt: " + str(alt)
		elif format == 'degrees':
			return "Azm: " + str(azm*360) + ", Alt: " + str(alt*360)
		elif format == 'H/DMS':
			azm_d, azm_m, azm_s  = _dd_to_dms(azm*360)
			alt_d, alt_m, alt_s = _dd_to_dms(alt*360)
			return ("Azm: " + str(azm_d) + "°" + str(azm_m) + "'" + str(azm_s) + '"'
				+ " Alt: " + str(alt_d) + "°" + str(alt_m) + "'" + str(alt_s) + '"')
		else:
			return msg_error_format
	else:
		return msg_error_check

#Hexadecimal value to fraction of revolution
def _hex_to_frac_of_rev(value):
	return int(value, 16) / 65536.0

#Precise hexadecimal value to fraction of revolution
def _hex_precise_to_frac_of_rev(value):
	return int(value, 16) / 4294967296.0

#Decimal degree to Hours:Minutes:Seconds
def _dd_to_hms(dd):
	hours = (dd/360.0)*24
	if 1 <= hours < 10:
		sHours = "0"+str(hours)[0]
	elif hours >= 10:
		sHours = str(hours)[:2]
	elif hours < 1:
		sHours = "00"

	if str(hours).find(".") == -1:
		mins = float(hours)*60.0
	else:
		mins = float(str(hours)[str(hours).index("."):])*60.0
	#if mins<10 and mins>=1:
	if 1 <= mins<10:
		sMins = "0"+str(mins)[:1]
	elif mins >= 10:
		sMins = str(mins)[:2]
	elif mins < 1:
		sMins = "00"

	secs = (hours-(float(sHours)+float(sMins)/60.0))*3600.0
	#if secs < 10 and secs>0.001:
	if 0.001 < secs < 10:
		sSecs = "0"+str(secs)[:str(secs).find(".")+4]
	elif secs < 0.0001:
		sSecs = "00.001"
	else:
		sSecs = str(secs)[:str(secs).find(".")+4]
	if len(sSecs) < 5:
		sSecs = sSecs+"00" # So all to 3dp

	if float(sSecs) == 60.000:
		sSecs = "00.00"
		sMins = str(int(sMins)+1)
	if int(sMins) == 60:
		sMins = "00"
		sDeg = str(int(sDeg)+1)

	return int(sHours), int(sMins), float(sSecs)

#Decimal degree to Degrees:Arcminutes:Arcseconds
def _dd_to_dms(dd):
	negative = dd < 0
	dd = abs(dd)
	minutes,seconds = divmod(dd*3600, 60)
	degrees,minutes = divmod(minutes, 60)
	if negative:
		if degrees > 0:
			degrees = -degrees
		elif minutes > 0:
			minutes = -minutes
		else:
			seconds = -seconds

	return int(degrees), int(minutes), seconds

##################################################################
#GOTO functions:                                                 #
# # ra: Right Ascension value								     #
# # dec: Declination value									     #
# # azm: Azimuth value	                                         #
# # alt: Altitude value									         #
# # format: Specifies format in that the coordinates are required #
##################################################################
def goto_RA_DEC(ra, dec, format):
	print ra, dec, format
	if echo(check) == check:
		if format == 'frac_of_rev':
			command = ('R' + _frac_of_rev_to_hex(ra) + ',' + _frac_of_rev_to_hex(dec))
		elif format == 'degrees':
			command = ('R' + _degrees_to_hex(ra) + ',' + _degrees_to_hex(dec))

		print command

		nexstar.write(command)
		response = nexstar.read(1)

		if response == "#":
			while is_goto_in_progress():
				continue
			else:
				return 'GOTO completed'
		else:
			return msg_error_goto
	else:
		return msg_error_check

def goto_precise_RA_DEC(ra, dec, format):
	if echo(check) == check:
		if format == 'frac_of_rev':
			command = ('r' + _frac_of_rev_to_hex_precise(ra) + ',' 
				+ _frac_of_rev_to_hex_precise(dec))
		elif format == 'degrees':
			command = ('r' + _degrees_to_hex_precise(ra) + ',' 
				+ _degrees_to_hex_precise(dec))

		nexstar.write(command)
		response = nexstar.read(1)

		if response == "#":
			while is_goto_in_progress():
				continue
			else:
				return 'GOTO completed'
		else:
			return msg_error_goto

	else:
		return msg_error_check

def goto_AZM_ALT(azm, alt, format):
	if echo(check) == check:
		if format == 'frac_of_rev':
			command = ('B' + _frac_of_rev_to_hex(azm) + ',' + _frac_of_rev_to_hex(alt))
		elif format == 'degrees':
			command = ('B' + _degrees_to_hex(azm) + ',' + _degrees_to_hex(alt))

		nexstar.write(command)
		response = nexstar.read(1)

		if response == "#":
			while is_goto_in_progress():
				continue
			else:
				return 'GOTO completed'
		else:
			return msg_error_goto

	else:
		return msg_error_check

def goto_precise_AZM_ALT(azm, alt, format):
	print 'Funcion goto_precise_AZM_ALT'
	print azm
	print _frac_of_rev_to_hex_precise(azm)
	print alt
	print _frac_of_rev_to_hex_precise(alt)
	if echo(check) == check:
		if format == 'frac_of_rev':
			command = ('b' + _frac_of_rev_to_hex_precise(azm) + ',' 
				+ _frac_of_rev_to_hex_precise(alt))
		elif format == 'degrees':
			command = ('b' + _degrees_to_hex_precise(azm) + ',' 
				+ _degrees_to_hex_precise(alt))

		nexstar.write(command)
		response = nexstar.read(1)

		if response == "#":
			while is_goto_in_progress():
				continue
			else:
				return 'GOTO completed'
		else:
			return msg_error_goto

	else:
		return msg_error_check

def _frac_of_rev_to_hex(value):
	return '%04X' % round(value * 2.**16)

def _frac_of_rev_to_hex_precise(value):	
	return '%08X' % round(value * 2.**32)

def _degrees_to_hex(value):
	return '%04X' % round(value / 360. * 2.**16)

def _degrees_to_hex_precise(value):
	return '%08X' % round(value / 360. * 2.**32)	

#################################################################
#GOTO functions with sexagesimal input                          #                                                #
# # ra_h: hours value of Right Ascension						#
# # ra_m: minutes value of Right Ascension						#
# # ra_s: seconds value of Right Ascension		  				#						
# # dec_d: degrees value of Declination							#
# # dec_m: arcminutes value of Declination						#
# # dec_s: arcseconds value of Declination						#										
# # azm_d: degrees value of Azimuth							    #
# # azm_m: arcminutes value of Azimuth					 	    #
# # azm_s: arcseconds value of Azimuth						    #
# # alt_d: degrees value of Altitude						    #
# # alt_m: arcminutes value of Altitude					 	    #
# # alt_s: arcseconds value of Altitude						    #
#################################################################
def goto_RA_DEC_hdms(ra_h, ra_m, ra_s, dec_d, dec_m, dec_s):
	ra_dd = _hms_to_dd(ra_h, ra_m, ra_s)
	dec_dd = _dms_to_dd(dec_d, dec_m,dec_s)

	return goto_precise_RA_DEC(ra_dd, dec_dd, 'degrees')

def goto_AZM_ALT_dms(azm_d, azm_m, azm_s, alt_d, alt_m, alt_s):
	azm_dd = _dms_to_dd(azm_d, azm_m, azm_s)
	alt_dd = _dms_to_dd(alt_d, alt_m, alt_s)

	return goto_precise_AZM_ALT(azm_dd, alt_dd, 'degrees')	

#Hours:Minutes_Seconds to decimal degrees
def _hms_to_dd(h, m, s):
	first = float(h) + float(m)/60.0 + float(s)/3600.0
	frac = first / 24
	degrees = frac * 360
	return degrees

#Degrees:Arcminutes:Arcseconds to decimal degrees
def _dms_to_dd(d, m, s):
	if d < 0:
		degrees = float(d) - float(m)/60.0 - float(s)/3600.0
	else:
		degrees = float(d) + float(m)/60.0 + float(s)/3600.0

	return degrees

###################################################################
#Sync functions:                                                  #
# # ra: Right Ascension value								      #
# # dec: Declination value									      #								         #
# # format: Specifies format in that the coordinates are required #
###################################################################
def sync_RA_DEC(ra, dec, format):
	if echo(check) == check:
		if format == 'frac_of_rev':
			command = ('S' + _frac_of_rev_to_hex(ra) + ',' + _frac_of_rev_to_hex(dec))
		elif format == 'degrees':
			command = ('S' + _degrees_to_hex(ra) + ',' + _degrees_to_hex(dec))

		nexstar.write(command)
		response = nexstar.read(1)

		return _verify_response(response)
	else:
		return msg_error_check

def sync_precise_RA_DEC(ra, dec, format):
	if echo(check) == check:
		if format == 'frac_of_rev':
			command = ('s' + _frac_of_rev_to_hex_precise(ra) + ',' 
				+ _frac_of_rev_to_hex_precise(dec))
		elif format == 'degrees':
			command = ('s' + _degrees_to_hex_precise(ra) + ',' 
				+ _degrees_to_hex_precise(dec))

		nexstar.write(command)
		response = nexstar.read(1)
		return _verify_response(response)
	else:
		return msg_error_check

#################################################################
#Sync function with sexagesimal input                           #                                                #
# # ra_h: hours value of Right Ascension						#
# # ra_m: minutes value of Right Ascension						#
# # ra_s: seconds value of Right Ascension		  				#						
# # dec_d: degrees value of Declination							#
# # dec_m: arcminutes value of Declination						#
# # dec_s: arcseconds value of Declination						#										
#################################################################
def sync_RA_DEC_hdms(ra_h, ra_m, ra_s, dec_d, dec_m, dec_s):
	ra_dd = _hms_to_dd(ra_h, ra_m, ra_s)
	dec_dd = _dms_to_dd(dec_d, dec_m,dec_s)

	return sync_precise_RA_DEC(ra_dd, dec_dd, 'degrees')

######################
#Tracking functions: #
## Tracking modes:   #
#	# 0 = Off        #
#	# 1 = Alt/Az     #
#	# 2 = EQ North   #
#	# 3 = EQ South   #
######################
def get_tracking_mode():
	if echo(check) == check:
		nexstar.write('t')
		response = nexstar.read(2)
		if ord(response[0]) == 0: #ord(): convierte un char en su valor ASCII
			output = '0 = Off'
		elif ord(response[0]) == 1:
			output = '1 = Alt/Az'
		elif ord(response[0]) == 2:
			output = '2 = EQ North'
		elif ord(response[0]) == 3:
			output = '3 = EQ South'
		return output
	else:
		return msg_error_check

def set_tracking_mode(mode):
	if echo(check) == check:
		nexstar.write('T' + chr(mode)) #chr: convierte ASCII a char
		response = nexstar.read(1)
		return _verify_response(response)
	else:
		return msg_error_check

############################################
#Slewing functions:                        #     
# # direction: Slew direction              #
# # sign: Slew sense                       #
# # rate: Slew rate [arcoseconds/seconds]  #
############################################
def slew_var_rate(direction, sign, rate):
	if echo(check) == check:
		if direction == 'azm_ra':
			direction_chr = chr(16)
		elif direction == 'alt_dec':
			direction_chr =  chr(17)

		if sign == 'negative':
			direction_sign_chr = chr(7)
		else:
			direction_sign_chr = chr(6)

		track_rate_high = (int(abs(rate)) * 4) / 256
		track_rate_low = (int(abs(rate)) * 4) % 256

		command = ('P' + chr(3) + direction_chr + direction_sign_chr +
			chr(track_rate_high) + chr(track_rate_low) + chr(0) + chr(0))

		nexstar.write(command)
		response = nexstar.read(1)
		return _verify_response(response)
	else:
		return msg_error_check

def slew_fixed_rate(direction, sign, rate):
	if echo(check) == check:
		if direction == 'azm_ra':
			direction_chr = chr(16)
		elif direction == 'alt_dec':
			direction_chr =  chr(17)

		if sign == 'negative':
			direction_sign_chr = chr(37)
		else:
			direction_sign_chr = chr(36)

		command = ('P' + chr(2) + direction_chr + direction_sign_chr +
			chr(rate) + chr(0) + chr(0) + chr(0))		

		nexstar.write(command)
		response = nexstar.read(1)
		return _verify_response(response)
	else:
		return msg_error_check

def stop_slewing():
	slew_fixed_rate('azm_ra', 'positive', 0)
	slew_fixed_rate('alt_dec', 'positive', 0)
	slew_var_rate('azm_ra', 'positive', 0)
	slew_var_rate('alt_dec', 'positive', 0)

	return 'Slewing has stopped'


#############################################################################################
#Time/location functions:                                                                   #
# # Location format is: ABCDEFGH, where:                                                    #
	# A is the number of degrees of latitude.                                               #
	# B is the number of minutes of latitude.                                               #
	# C is the number of seconds of latitude.                                               #
	# D is 0 for north and 1 for south.                                                     #
	# E is the number of degrees of longitude.                                              #
	# F is the number of minutes of longitude.                                              #
	# G is the number of seconds of longitude.                                              #
	# H is 0 for east and 1 for west.                                                       #
# # Time format is: QRSTUVWX, where:                                                        #
	# Q is the hour (24 hour clock).                                                        #
	# R is the minutes.                                                                     #
	# S is the seconds.                                                                     #
	# T is the month.                                                                       #
	# U is the day.                                                                         #
	# V is the year (century assumed as 20).                                                #
	# W is the offset from GMT for the time zone. Note: if zone is negative, use 256-zone.  #
	# X is 1 to enable Daylight Savings and 0 for Standard Time.                            #
#############################################################################################
def get_location():
	if echo(check) == check:
		nexstar.write('w')
		response = nexstar.read(9)
		A = ord(response[0])
		B = ord(response[1])
		C = ord(response[2])
		D = 'N' if ord(response[3]) == 0 else 'S'
		latitude = (str(A) + '°' + str(B) + "'" + str(C) + '"' + str(D))

		E = ord(response[4])
		F = ord(response[5])
		G = ord(response[6])
		H = 'E' if ord(response[7]) == 0 else 'W'
		longitude = (str(E) + '°' + str(F) + "'" + str(G) + '"' + str(H))

		return (latitude + ', ' + longitude)
	else:
		return msg_error_check

def set_location(A, B, C, D, E, F, G, H):
	if echo(check) == check:
		command = ('W' + chr(A) + chr(B) + chr(C) + chr(D) + chr(E) + chr(F) + chr(G) + chr(H))
		nexstar.write(command)
		response = nexstar.read(1)
		return _verify_response(response)
	else:
		return msg_error_check

def get_time():
	if echo(check) == check:
		nexstar.write('h')
		response = nexstar.read(9)
		Q = ord(response[0]) #Hours
		R = ord(response[1]) #Minutes
		S = ord(response[2]) #Seconds
		T = ord(response[3]) #Month
		U = ord(response[4]) #Day
		V = ord(response[5]) #Year
		W = ord(response[6]) #Offset from GMT (Santiago, Chile = GMT-3)
		if W > 14: #Zona horaria negativa
			time_zone = 'GMT - ' + str(256 - W)
		else:
			time_zone = 'GMT + ' + W		
		X = ord(response[7]) #1: enable Daylight Savings, 0: Standard Time
		if X == 0:
			time_type = 'Standard Time'
		else:
			time_type = 'Daylight Savings'

		return (str(Q) + ':' + str(R) + ':' + str(S) + ' ' +
			str(U) + '/' + str(T) + '/' + str(V) + ' ' +
			time_zone + ' ' + time_type)
	else:
		return msg_error_check

def set_time(Q, R, S, T, U, V, W, X):
	if echo(check) == check:
		if W < 0:
			W = 256 + W

		command = ('H' + chr(Q) + chr(R) + chr(S) + chr(T) + chr(U) + chr(V) + chr(W) + chr(X))
		nexstar.write(command)
		response =  nexstar.read(1)
		return _verify_response(response)
	else:
		return msg_error_check


###################################################################
#GPS functions:                                                   #
# # format: Specifies format in that the coordinates are required #
###################################################################
def is_gps_linked():
	if echo(check) == check:
		command = ('P' + chr(1) + chr(176) + chr(55) + chr(0) + chr(0)
			 + chr(0) + chr(1))
		nexstar.write(command)
		response = nexstar.read(2)
		print int(ord(response[0]))

		if int(ord(response[0])) == 0:
			output = 'GPS Not Linked'
		elif int(ord(response[0])) > 0:
			output = 'GPS Linked'

		return output
	else:
		msg_error_check

def gps_get_latitude(format):
	if echo(check) == check:
		if is_gps_linked() == 'GPS Not Linked':
			return 'Error: GPS Not Linked'
		else:
			command = ('P' + chr(1) + chr(176) + chr(1) + chr(0) + chr(0)
				 + chr(0) + chr(3))
			nexstar.write(command)
			response = nexstar.read(4)
			print response
			print response[3]

			latitude = (ord(response[0]) * 2.**16 + ord(response[1]) * 2.**8 +
				ord(response[2])) / (2.**24)

			if format == 'frac_of_rev':
				return latitude
			elif format == 'degrees':
				return latitude * 360
	else:
		return msg_error_check

def gps_get_longitude(format):
	if echo(check) == check:
		if is_gps_linked() == 'GPS Not Linked':
			return 'Error: GPS Not Linked'
		else:
			command = ('P' + chr(1) + chr(176) + chr(2) + chr(0) + chr(0)
				 + chr(0) + chr(3))
			nexstar.write(command)
			response = nexstar.read(4)
			print response
			print response[3]

			longitude = (ord(response[0]) * 2.**16 + ord(response[1]) * 2.**8 +
				ord(response[2])) / (2.**24)

			if format == 'frac_of_rev':
				return longitude
			elif format == 'degrees':
				return longitude * 360
	else:
		return msg_error_check

def gps_get_date():
	if echo(check) == check:
		if is_gps_linked() == 'GPS Not Linked':
			return 'Error: GPS Not Linked'
		else:
			command = ('P' + chr(1) + chr(176) + chr(3) + chr(0) + chr(0)
				 + chr(0) + chr(2))
			nexstar.write(command)
			response = nexstar.read(3)

			month = ord(response[0])
			day = ord(response[1])

			year_command = ('P' + chr(1) + chr(176) + chr(4) + chr(0) + chr(0)
				 + chr(0) + chr(2))
			nexstar.write(year_command)
			year_response = nexstar.read(3)

			year = (ord(year_response[0]) * 2.**8 + ord(year_response[1]))

			return (str(day) + '/' + str(month) + '/' + str(year))
	else:
		return msg_error_check

def gps_get_time():
	if echo(check) == check:
		if is_gps_linked() == 'GPS Not Linked':
			return 'Error: GPS Not Linked'
		else:
			command = ('P' + chr(1) + chr(176) + chr(51) + chr(0) + chr(0)
				 + chr(0) + chr(3))
			nexstar.write(command)
			response = nexstar.read(4)

			hours = ord(response[0])
			minutes = ord(response[1])
			seconds = ord(response[2])

			return (str(hours) + ':' + str(minutes) + ':' + str(seconds))
	else:
		return msg_error_check


############################
#RTC (CGE Mount) functions:#
############################
def rtc_get_date():
	if echo(check) == check:
		command = ('P' + chr(1) + chr(178) + chr(3) + chr(0) + chr(0)
			 + chr(0) + chr(2))
		nexstar.write(command)
		response = nexstar.read(3)

		month = ord(response[0])
		day = ord(response[1])

		nexstar.write('P' + chr(1) + chr(178) + chr(4) + chr(0) + chr(0)
			 + chr(0) + chr(2))
		year_response = nexstar.read(3)

		year = (ord(year_response[0]) * 2.**8 + ord(year_response[1]))

		return (str(day) + '/' + str(month) + '/' + str(year))
	else:
		return msg_error_check

def rtc_get_time():
	if echo(check) == check:
		command = ('P' + chr(1) + chr(178) + chr(51) + chr(0) + chr(0)
			 + chr(0) + chr(3))
		nexstar.write(command)
		response = nexstar.read(4)

		hours = ord(response[0])
		minutes = ord(response[1])
		seconds = ord(response[2])

		#Formatear correctamente el tiempo
		if hours < 10:
			hours = str(0) + str(hours)
		if minutes < 10:
			minutes = str(0) + str(minutes)

		if seconds < 10:
			seconds = str(0) + str(seconds)

		return (str(hours) + ':' + str(minutes) + ':' + str(seconds))
	else:
		return msg_error_check

def rtc_set_date(day, month, year):
	if echo(check) == check:
		command = ('P' + chr(3) + chr(178) + chr(131) + chr(month) +
			chr(day) + chr(0) + chr(0))
		nexstar.write(command)
		response = nexstar.read(1)
		return _verify_response(response)
	else:
		return msg_error_check

def rtc_set_time(hours, minutes, seconds):
	if echo(check) == check:
		command = ('P' + chr(4) + chr(178) + chr(179) + 
			chr(hours) + chr(minutes) + chr(seconds) + chr(0))
		nexstar.write(command)
		response =  nexstar.read(1)
		return _verify_response(response)
	else:
		return msg_error_check