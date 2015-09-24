#!/usr/bin/env python
#-*- coding: utf-8 -*-


import sys
import requests

KEY = 'b90eda14-6a5f-44d9-8b9a-adb8b507d248'

def getMTAdetailed(key, route, path):
	'''prints bust route
	info from NY MTA API'''
	
	link = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json'
	payload = {'key':key, 'VehicleMonitoringDetailLevel':'calls', 'LineRef':route }
	
	answer  = requests.get(link, params=payload).json()
	
	Active_buses = answer['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

	print '\nBus Line : %s' % route
	print 'Number of Active Buses : %d' % len(Active_buses)
	
	for i, bus in enumerate(Active_buses):
		lat = bus['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
		lon = bus['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
		print 'Bus %d is at latitude %f and longitude %f' % (i, lat, lon)

if __name__ == '__main__':
	getMTA(sys.argv[1],sys.argv[2], sys.argv[3] )

# getMTA(KEY, 'B52')
