#!/usr/bin/python
# -*- coding: UTF-8 -*-

import serial, io, math

#Parametros para conexion serial con Telescopio
device = '/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller-if00-port0';

#Se establece conexión serial con el Telescopio, la instancia de la conexión se pasa a la variable "nexstar"
nexstar = serial.Serial(device, baudrate=9600, timeout=1)

check = 1
msg_error_check = 'Communication problem, check the conections and make sure that the telescope is on'
msg_error_format = 'Error: Invalid format'
msg_error_goto = 'Error: A problem has ocurred with the GOTO command, check the values and try again'

###########################################################################
#Funciones Get Position:												  #
# #format: especifíca en qué formato se requieren las coordenadas         #
#		- 'percent_of_rev': Porcentaje de revolución					  #	
#		- 'degrees': Grados 											  #
#		- 'H/DMS': Horas/Grados:Minutos/Arcominutos:Segundos/Arcosegundos #
###########################################################################
def get_RA_DEC(format):
	if echo(check) == check:
		nexstar.write('E')
		response = nexstar.read(10) #Se espera respuesta de 10 bytes
		print 'get_RA_DEC: '
		print response
		print response[0:4]
		print response[5:9]

		ra = _hex_to_perc_of_rev(response[0:4])
		dec = _hex_to_perc_of_rev(response[5:9])

		print ra
		print dec

		if format == 'percent_of_rev':
			#return ra, dec
			return "RA: " + str(ra) + ", DEC: " + str(dec)
		elif format == 'degrees':
			#return ra * 360, dec * 360
			return "RA: " + str(ra*360) + ", DEC: " + str(dec*360)
		elif format == 'H/DMS':
			ra_h, ra_m, ra_s  = _dd_to_hms(ra*360)
			dec_d, dec_m, dec_s = _dd_to_dms(dec*360)
			#return ra_h, ra_m, ra_s, dec_d, dec_m, dec_s
			return ("RA: " + str(ra_h) + "h" + str(ra_m) + "m" + str(ra_s) + "s"
				+ " DEC: " + str(dec_d) + "°" + str(dec_m) + "'" + str(dec_s) + '"')
		else:
			return msg_error_format
	else:
		return msg_error_check



def get_precise_RA_DEC(format):
	if echo(check) == check:
		nexstar.write('e')
		response = nexstar.read(18) #Se espera respuesta de 18 bytes

		ra = _hex_precise_to_perc_of_rev(response[0:8])
		dec = _hex_precise_to_perc_of_rev(response[9:17])

		if format == 'percent_of_rev':
			return "RA: " + str(ra) + ", DEC: " + str(dec)
		elif format == 'degrees':
			return "RA: " + str(ra*360) + ", DEC: " + str(dec*360)
		elif format == 'H/DMS':
			ra_h, ra_m, ra_s  = _dd_to_hms(ra*360)
			dec_d, dec_m, dec_s = _dd_to_dms(dec*360)
			return ("RA: " + str(ra_h) + "h" + str(ra_m) + "m" + str(ra_s) + "s"
				+ " DEC: " + str(dec_d) + "°" + str(dec_m) + "'" + str(dec_s) + '"')
		else:
			return msg_error_format
	else:
		return msg_error_check

def get_AZM_ALT(format):
	if echo(check) == check:
		nexstar.write('Z')
		response = nexstar.read(10) #Se espera respuesta de 10 bytes

		azm = _hex_to_perc_of_rev(response[0:4])
		alt = _hex_to_perc_of_rev(response[5:9])

		if format == 'percent_of_rev':
			return "AZM: " + str(azm) + ", ALT: " + str(alt)
		elif format == 'degrees':
			return "AZM: " + str(azm*360) + ", ALT: " + str(alt*360)
		elif format == 'H/DMS':
			azm_d, azm_m, azm_s  = _dd_to_dms(azm*360)
			alt_d, alt_m, alt_s = _dd_to_dms(alt*360)
			return ("AZM: " + str(azm_d) + "°" + str(azm_m) + "'" + str(azm_s) + '"'
				+ " ALT: " + str(alt_d) + "°" + str(alt_m) + "'" + str(alt_s) + '"')
		else:
			return msg_error_format
	else:
		return msg_error_check

def get_precise_AZM_ALT(format):
	if echo(check) == check:
		nexstar.write('z')
		response = nexstar.read(18) #Se espera respuesta de 18 bytes

		azm = _hex_precise_to_perc_of_rev(response[0:8])
		alt = _hex_precise_to_perc_of_rev(response[9:17])

		if format == 'percent_of_rev':
			return "AZM: " + str(azm) + ", ALT: " + str(alt)
		elif format == 'degrees':
			return "AZM: " + str(azm*360) + ", ALT: " + str(alt*360)
		elif format == 'H/DMS':
			azm_d, azm_m, azm_s  = _dd_to_dms(azm*360)
			alt_d, alt_m, alt_s = _dd_to_dms(alt*360)
			return ("AZM: " + str(azm_d) + "°" + str(azm_m) + "'" + str(azm_s) + '"'
				+ " ALT: " + str(alt_d) + "°" + str(alt_m) + "'" + str(alt_s) + '"')
		else:
			return msg_error_format
	else:
		return msg_error_check

#Valor hexadecimal a fracción de revolución
def _hex_to_perc_of_rev(value):
	return int(value, 16) / 65536.0

#Valor hexadecimal preciso a fracción de revolución
def _hex_precise_to_perc_of_rev(value):
	return int(value, 16) / 4294967296.0

#Grado decimal a Horas:Minutos:Segundos
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

	#(hfrac, hours) = math.modf(dd)
	#(mfrac, minutes) = math.modf(hfrac * 60)
	#seconds = mfrac * 60.
	#return (str(int(hours)) + 'h' + str(int(minutes)) + 'm' + str(seconds) + 's')
	#return int(hours), int(minutes), seconds

#Grado decimal a Grados:Arcominutos:Arcosegundos
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

#################################################################
#Funciones GOTO:                                                #
# #ra: valor de Right Ascension								    #
# #dec: valor de Declination									#
# #azm: valor de Azimuth	                                    #
# #alt: valor de Altitude									    #
# #format: especifíca en qué formato se reciben las coordenadas #
#################################################################
def goto_RA_DEC(ra, dec, format):
	if echo(check) == check:
		if format == 'percent_of_rev':
			command = ('R' + _perc_of_rev_to_hex(ra) + ',' + _perc_of_rev_to_hex(dec))
		elif format == 'degrees':
			command = ('R' + _degrees_to_hex(ra) + ',' + _degrees_to_hex(dec))

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
		if format == 'percent_of_rev':
			command = ('r' + _perc_of_rev_to_hex_precise(ra) + ',' 
				+ _perc_of_rev_to_hex_precise(dec))
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
		if format == 'percent_of_rev':
			command = ('B' + _perc_of_rev_to_hex(azm) + ',' + _perc_of_rev_to_hex(alt))
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
	print _perc_of_rev_to_hex_precise(azm)
	print alt
	print _perc_of_rev_to_hex_precise(alt)
	if echo(check) == check:
		if format == 'percent_of_rev':
			command = ('b' + _perc_of_rev_to_hex_precise(azm) + ',' 
				+ _perc_of_rev_to_hex_precise(alt))
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

def _perc_of_rev_to_hex(value):
	return '%04X' % round(value * 2.**16)

def _perc_of_rev_to_hex_precise(value):	
	return '%08X' % round(value * 2.**32)

def _degrees_to_hex(value):
	return '%04X' % round(value / 360. * 2.**16)

def _degrees_to_hex_precise(value):
	return '%08X' % round(value / 360. * 2.**32)	

#################################################################
#Funciones GOTO con parámetros de entrada como h:m:s y °:':"    #                                                #
# #ra_h: hours value of Right Ascension							#
# #ra_m: minutes value of Right Ascension						#
# #ra_s: seconds value of Right Ascension		  				#						
# #dec_d: degrees value of Declination							#
# #dec_m: arcminutes value of Declination						#
# #dec_s: arcseconds value of Declination						#										
# #azm_d: degrees value of Azimuth							    #
# #azm_m: arcminutes value of Azimuth					 	    #
# #azm_s: arcseconds value of Azimuth						    #
# #alt_d: degrees value of Altitude						        #
# #alt_m: arcminutes value of Altitude					 	    #
# #alt_s: arcseconds value of Altitude						    #
#################################################################
def goto_RA_DEC_hdms(ra_h, ra_m, ra_s, dec_d, dec_m, dec_s):
	ra_dd = _hms_to_dd(ra_h, ra_m, ra_s)
	dec_dd = _dms_to_dd(dec_d, dec_m,dec_s)

	return goto_precise_RA_DEC(ra_dd, dec_dd, 'degrees')

def goto_AZM_ALT_dms(azm_d, azm_m, azm_s, alt_d, alt_m, alt_s):
	azm_dd = _dms_to_dd(azm_d, azm_m, azm_s)
	alt_dd = _dms_to_dd(alt_d, alt_m, alt_s)

	return goto_precise_AZM_ALT(azm_dd, alt_dd, 'degrees')	

#Horas:Minutos:Segundos a grado decimal
def _hms_to_dd(h, m, s):
	first = float(h) + float(m)/60.0 + float(s)/3600.0
	percent = first / 24
	degrees = percent * 360
	return degrees

#Grados:Arcominutos:Arcosegundos a grado decimal
def _dms_to_dd(d, m, s):
	if d < 0:
		degrees = float(d) - float(m)/60.0 - float(s)/3600.0
	else:
		degrees = float(d) + float(m)/60.0 + float(s)/3600.0

	return degrees

#################
#Funciones Sync:#
#################
def sync_RA_DEC(ra, dec, format):
	if echo(check) == check:
		if format == 'percent_of_rev':
			command = ('S' + _perc_of_rev_to_hex(ra) + ',' + _perc_of_rev_to_hex(dec))
		elif format == 'degrees':
			command = ('S' + _degrees_to_hex(ra) + ',' + _degrees_to_hex(dec))

		nexstar.write(command)
		response = nexstar.read(1)

		return _verify_response(response)
	else:
		return msg_error_check

def sync_precise_RA_DEC(ra, dec, format):
	if echo(check) == check:
		if format == 'percent_of_rev':
			command = ('s' + _perc_of_rev_to_hex_precise(ra) + ',' 
				+ _perc_of_rev_to_hex_precise(dec))
		elif format == 'degrees':
			command = ('s' + _degrees_to_hex_precise(ra) + ',' 
				+ _degrees_to_hex_precise(dec))

		nexstar.write(command)
		response = nexstar.read(1)
		return _verify_response(response)
	else:
		return msg_error_check

def sync_RA_DEC_hdms(ra_h, ra_m, ra_s, dec_d, dec_m, dec_s):
	ra_dd = _hms_to_dd(ra_h, ra_m, ra_s)
	dec_dd = _dms_to_dd(dec_d, dec_m,dec_s)

	return sync_precise_RA_DEC(ra_dd, dec_dd, 'degrees')

#####################
#Funciones Tracking:#
#####################
	#Tracking modes:
		# 0 = Off
		# 1 = Alt/Az
		# 2 = EQ North
		# 3 = EQ South
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

####################
#Funciones Slewing:#
####################
#Recibe direction: azm_ra o alt_dec y rate en arcseconds/second
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


##########################
#Funciones Time/location:#
##########################
#El formato para los comandos de Location es: ABCDEFGH, donde:
	#A is the number of degrees of latitude.
	#B is the number of minutes of latitude.
	#C is the number of seconds of latitude.
	#D is 0 for north and 1 for south.
	#E is the number of degrees of longitude.
	#F is the number of minutes of longitude.
	#G is the number of seconds of longitude.
	#H is 0 for east and 1 for west.
#El formato para los comandos de Time es: QRSTUVWX, donde:
	#Q is the hour (24 hour clock).
	#R is the minutes.
	#S is the seconds.
	#T is the month.
	#U is the day.
	#V is the year (century assumed as 20).
	#W is the offset from GMT for the time zone. Note: if zone is negative, use 256-zone.
	#X is 1 to enable Daylight Savings and 0 for Standard Time.

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
		H = 'E' if ord(response[3]) == 0 else 'W'
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

#Se recibe Time con el siguiente formato: (HH,MM,SS,DD,MM,YY,GMT_Offset,type) 
def set_time(Q, R, S, T, U, V, W, X):
	if echo(check) == check:
		if W < 0:
			W = 256 + W

		command = ('W' + chr(Q) + chr(R) + chr(S) + chr(T) + chr(U) + chr(V) + chr(W) + chr(X))
		nexstar.write(command)
		response =  nexstar.read(1)
		return _verify_response(response)
	else:
		return msg_error_check


################
#Funciones GPS:#
################
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

			if format == 'percent_of_rev':
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

			if format == 'percent_of_rev':
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
#Funciones RTC (CGE Mount):#
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

		#DUDA CON SET YEAR!
		#nexstar.write('P' + chr(3) + chr(178) + chr(132) + chr(month) +
		#	chr(day) + chr(0) + chr(0))
		#response = nexstar.read(1)
		#_verify_response(response)
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


########################
#Funciones Misceláneas:#
########################
def get_version():
	if echo(check) == check:
		nexstar.write('V')
		response = nexstar.read(3)
		if response[2] == '#':
			return 'Major: ' + str(ord(response[0])) + ', minor: ' + str(ord(response[1]))
		else:
			return 'Error: The telescope has send wrong information'
	else:
		return msg_error_check

def get_device_version(device):
	if echo(check) == check:
		if device == 'AZM/RA Motor':
			dev = 16
		elif device == 'ALT/DEC Motor':
			dev = 17
		elif device == 'GPS Unit':
			dev = 176
		elif device == 'RTC':
			dev = 178
		else:
			return 'Error: Invalid device'

		command = ('P' + chr(1) + chr(dev) + chr(254) + chr(0) + 
			chr(0) + chr(0) + chr(2))
		nexstar.write(command)
		response = nexstar.read(3)
		return 'Major: ' + str(ord(response[0])) + ', minor: ' + str(ord(response[1]))
	else:
		return msg_error_check

def get_model():
	if echo(check) == check:
		nexstar.write('m')
		response = nexstar.read(2)

		model = ord(response[0])
		if model == 1:
			return 'GPS Series'
		elif model == 3:
			return 'i-Series'
		elif model == 4:
			return 'i-Series SE'
		elif model == 5:
			return 'CGE'
		elif model == 6:
			return 'Advanced GT'
		elif model == 7:
			return 'SLT'
		elif model == 9:
			return 'CPC'
		elif model == 10:
			return 'GT'
		elif model == 11:
			return '4/5 SE'
		elif model == 12:
			return '6/8 SE'
		else:
			return 'Modelo desconocido (model id: ' + str(ord(response[0])) + ')'
	else:
		return msg_error_check

#Para chequear comunicación
def echo(x):
	command = ('K' + chr(x))
	nexstar.write(command)
	response = nexstar.read(2)
	return ord(response[0])

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

