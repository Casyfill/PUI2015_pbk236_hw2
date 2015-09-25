# PUI2015_pbk236_hw2
another homework for PUI CUSP 2015

##Assignment 1: show_bus_locations.py

####Dependencies:
I use *[requests](http://docs.python-requests.org/)* module instead of urllib. It can be easily installed via *pip*

####Info

This script prints all active (displayed through API) buses for specified route, as well as location for each

to activate enter this:
	**python show_bus_locations.py xxxx-xxxx-xxxx-xxxx-xxxx B52**


##Assignment 2: get_bus_info.py

####Dependencies:
I use *[requests](http://docs.python-requests.org/)* module instead of urllib. It can be easily installed via *pip*

####Info

This script prints all active (displayed through API) buses for specified route, as well as location and next station for each, and write following info to .csv file: lon, lat, stop name, distance to stop (in stops)

to activate enter this:
	**python get_bus_info.py xxxx-xxxx-xxxx-xxxx-xxxx M7 M7.csv**




