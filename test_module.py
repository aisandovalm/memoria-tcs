#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import telescope, camera

#sys.argv[0] es el nombre del script

#Valores por default:
#Porcentaje de revolución
ra_percent = 0.2
dec_percent = 0.5
azm_percent = 0.1
alt_percent = 0.4
#Grados
ra_degrees = 45
dec_degrees = 45
azm_degrees = 200
alt_degrees = -10
#Horas:Minutos:Segundos
ra_h = 9
ra_m = 39
ra_s = 31.40
#Grados:Arcominutos:Arcosegundos
dec_d = 14
dec_m = 20
dec_s = 41.2
azm_d = 342
azm_m = 52
azm_s = 31.8
alt_d = 40
alt_m = 13
alt_s = 22.5

#########################
#Funciones Get Position:#
#########################
if sys.argv[1] == 'get_RA_DEC':
	print 'RA, DEC en porcentaje de revolución:'
	print telescope.get_RA_DEC('percent_of_rev')

	print 'RA, DEC en grados:'
	print telescope.get_RA_DEC('degrees')

	print 'RA en horas:minutos:segundos, DEC en grados:arcominutos:arcosegundos :'
	h, m, s, d, _m, _s = telescope.get_RA_DEC('H/DMS')
	ra = str(h) + 'h' + str(m) + 'm' + str(s) + 's'
	dec = str(d) + '°' + str(_m) + "'" + str(_s) + '"'
	print ra, dec

elif sys.argv[1] == 'get_precise_RA_DEC':
	print 'RA, DEC preciso en porcentaje de revolución:'
	print telescope.get_precise_RA_DEC('percent_of_rev')

	print 'RA, DEC preciso en grados:'
	print telescope.get_precise_RA_DEC('degrees')

	print 'RA preciso en horas:minutos:segundos, DEC preciso en grados:arcominutos:arcosegundos :'
	h, m, s, d, _m, _s = telescope.get_precise_RA_DEC('H/DMS')
	ra = str(h) + 'h' + str(m) + 'm' + str(s) + 's'
	dec = str(d) + '°' + str(_m) + "'" + str(_s) + '"'
	print ra, dec

elif sys.argv[1] == 'get_AZM_ALT':
	print 'AZM, ALT en porcentaje de revolución:'
	print telescope.get_AZM_ALT('percent_of_rev')

	print 'AZM, ALT en grados:'
	print telescope.get_AZM_ALT('degrees')

	print 'AZM, ALT en grados:arcominutos:arcosegundos :'
	d, m, s, _d, _m, _s = telescope.get_AZM_ALT('DMS')

	azm = str(d) + '°' + str(m) + "'" + str(s) + '"'
	alt = str(_d) + '°' + str(_m) + "'" + str(_s) + '"'
	print azm, alt

elif sys.argv[1] == 'get_precise_AZM_ALT':
	print 'AZM, ALT preciso en porcentaje de revolución:'
	print telescope.get_precise_AZM_ALT('percent_of_rev')

	print 'AZM, ALT preciso en grados:'
	print telescope.get_precise_AZM_ALT('degrees')

	print 'AZM, ALT preciso en grados:arcominutos:arcosegundos:'
	d, m, s, _d, _m, _s = telescope.get_precise_AZM_ALT('DMS')

	azm = str(d) + '°' + str(m) + "'" + str(s) + '"'
	alt = str(_d) + '°' + str(_m) + "'" + str(_s) + '"'
	print azm, alt	

#########################
#Funciones GOTO:#
#########################
elif sys.argv[1] == 'goto_RA_DEC':
	if len(sys.argv) == 5: #Se entregan las coordenadas y el formato
		response = telescope.goto_RA_DEC(float(sys.argv[2]), float(sys.argv[3]), sys.argv[4])
	elif len(sys.argv) == 3: #Solo se entrega el formato
		if sys.argv[2] == 'percent_of_rev':
			response = telescope.goto_RA_DEC(ra_percent, dec_percent, 'percent_of_rev')
		elif sys.argv[2] == 'degrees':
			response = telescope.goto_RA_DEC(ra_degrees, dec_degrees, 'degrees')

	print response

elif sys.argv[1] == 'goto_precise_RA_DEC':
	if len(sys.argv) == 5: #Se entregan las coordenadas y el formato
		response = telescope.goto_precise_RA_DEC(float(sys.argv[2]), float(sys.argv[3]), sys.argv[4])
	elif len(sys.argv) == 3: #Solo se entrega el formato
		if sys.argv[2] == 'percent_of_rev':
			response = telescope.goto_precise_RA_DEC(ra_percent, dec_percent, 'percent_of_rev')
		elif sys.argv[2] == 'degrees':
			response = telescope.goto_precise_RA_DEC(ra_degrees, dec_degrees, 'degrees')

	print response

elif sys.argv[1] == 'goto_AZM_ALT':
	if len(sys.argv) == 5: #Se entregan las coordenadas y el formato
		response = telescope.goto_AZM_ALT(float(sys.argv[2]), float(sys.argv[3]), sys.argv[4])
	elif len(sys.argv) == 3: #Solo se entrega el formato
		if sys.argv[2] == 'percent_of_rev':
			response = telescope.goto_AZM_ALT(azm_percent, alt_percent, 'percent_of_rev')
		elif sys.argv[2] == 'degrees':
			response = telescope.goto_AZM_ALT(azm_degrees, alt_degrees, 'degrees')

	print response

elif sys.argv[1] == 'goto_precise_AZM_ALT':
	if len(sys.argv) == 5: #Se entregan las coordenadas y el formato
		response = telescope.goto_precise_AZM_ALT(float(sys.argv[2]), float(sys.argv[3]), sys.argv[4])
	elif len(sys.argv) == 3: #Solo se entrega el formato
		if sys.argv[2] == 'percent_of_rev':
			response = telescope.goto_precise_AZM_ALT(azm_percent, alt_percent, 'percent_of_rev')
		elif sys.argv[2] == 'degrees':
			response = telescope.goto_precise_AZM_ALT(azm_degrees, alt_degrees, 'degrees')

	print response	

elif sys.argv[1] == 'cancel_goto':
	response = telescope.cancel_goto()
	print response

#################
#Funciones Sync:#
#################
elif sys.argv[1] == 'sync_RA_DEC':
	if len(sys.argv) == 5: #Se entregan las coordenadas y el formato
		response = telescope.sync_RA_DEC(float(sys.argv[2]), float(sys.argv[3]), sys.argv[4])
	elif len(sys.argv) == 3: #Solo se entrega el formato
		if sys.argv[2] == 'percent_of_rev':
			response = telescope.sync_RA_DEC(0.20573, 0.07346, 'percent_of_rev')
		elif sys.argv[2] == 'degrees':
			response = telescope.sync_RA_DEC(74.0628, 26.4456, 'degrees')

	print response	

elif sys.argv[1] == 'sync_precise_RA_DEC':
	if len(sys.argv) == 5: #Se entregan las coordenadas y el formato
		response = telescope.sync_precise_RA_DEC(float(sys.argv[2]), float(sys.argv[3]), sys.argv[4])
	elif len(sys.argv) == 3: #Solo se entrega el formato
		if sys.argv[2] == 'percent_of_rev':
			response = telescope.sync_precise_RA_DEC(0.205734550, 0.073456108, 'percent_of_rev')
		elif sys.argv[2] == 'degrees':
			response = telescope.sync_precise_RA_DEC(74.064438, 26.44419888, 'degrees')

	print response	

#####################
#Funciones Tracking:#
#####################
	#Tracking modes:
		# 0 = Off
		# 1 = Alt/Az
		# 2 = EQ North
		# 3 = EQ South
elif sys.argv[1] == 'get_tracking_mode':
	response = telescope.get_tracking_mode()
	print 'Tracking mode: ' + response		

elif sys.argv[1] == 'set_tracking_mode':
	response = telescope.set_tracking_mode(int(sys.argv[2]))
	print response

####################
#Funciones Slewing:#
####################
elif sys.argv[1] == 'slew_var_rate':
	if sys.argv[2] == 'azm_ra':
		response = telescope.slew_var_rate('azm_ra', 0)
	elif sys.argv[2] == 'alt_dec':
		response = telescope.slew_var_rate('alt_dec', 150)

	print response

#print telescope.get_RA_DEC('degrees')

#print telescope.get_AZM_ALT('degrees')

#telescope.goto_AZM_ALT(45, 45, 'degrees')

#print telescope.get_AZM_ALT('degrees')
