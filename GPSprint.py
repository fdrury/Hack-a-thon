import gps, os, time

session = gps.gps(host="localhost",port="2947")

session.poll()

session.stream()

while 1:
	
	os.system("clear")
	
	session.poll()
	
	print
	
	print "GPS reading"
	
	print"---------"
	
	print "lat", session.fix.latitude
	
	print "lon", session.fix.longitude
	
	print "time utc", session.utc, session.fix.time
	
	print "Satellites (total of", len(session.satellites), "in view)"
	
	time.sleep(1)
