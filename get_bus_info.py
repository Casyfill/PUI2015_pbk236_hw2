#!/usr/bin/env python
#-*- coding: utf-8 -*-


import sys
import requests
import csv


def getMTAdetailed(key, route, path):
    '''prints bust route
    info from NY MTA API'''

    link = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json'
    payload = {
        'key': key, 'VehicleMonitoringDetailLevel': 'calls', 'LineRef': route}

    answer = requests.get(link, params=payload).json()

    Active_buses = answer['Siri']['ServiceDelivery'][
        'VehicleMonitoringDelivery'][0]['VehicleActivity']

    # print '\nBus Line : %s' % route
    # print 'Number of Active Buses : %d' % len(Active_buses)

    rows = []  # list for each bus dictionary

    for bus in Active_buses:
        lat = bus['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        lon = bus['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        'N/A'
        

        if len(bus['MonitoredVehicleJourney']["OnwardCalls"])>0:
	        stop = bus['MonitoredVehicleJourney'][
	            "OnwardCalls"]["OnwardCall"][0]['StopPointName']
	        stopStatus = bus['MonitoredVehicleJourney']["OnwardCalls"][
	            "OnwardCall"][0]['Extensions']['Distances']['PresentableDistance']
	    else:
	    	stop, stopStatus = 'N/A', 'N/A'


        busInfo = {'Latitude': lat, "Longitude": lon,
                   'Stop Name': stop, 'Stop Status': stopStatus}
        rows.append(busInfo)
        # print 'Bus %d is at latitude %f and longitude %f' % (i, lat, lon)

    headersList = ['Latitude', 'Longitude', 'Stop Name', 'Stop Status']

    with open(path, 'wb') as writeFile:
        wD = csv.DictWriter(
            writeFile, headersList, restval='', extrasaction='raise', dialect='excel')
        wD.writeheader()

        for row in rows:
            wD.writerow(row)


# getMTAdetailed(KEY, 'B52', 'p')
if __name__ == '__main__':
    getMTAdetailed(sys.argv[1], sys.argv[2], sys.argv[3])


