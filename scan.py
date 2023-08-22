import pyinsane2
pyinsane2.init()
devices = pyinsane2.get_devices()
print(devices) # prints the list of scanners
scanner = devices[0] # selects the first scanner
scan_session = scanner.scan(multiple=False) # starts a single scan
pyinsane2.exit()
