import pyinsane2

pyinsane2.init()
devices = pyinsane2.get_devices()
assert(len(devices) > 0)
device = devices[0]
print("I'm going to use the following scanner: %s" % (str(device)))
scanner_id = device.name
pyinsane2.exit()

pyinsane2.init()
devices = pyinsane2.get_devices()
assert(len(devices) > 0)
device = devices[0]
print("I'm going to use the following scanner: %s" % (str(device)))
scan_session = device.scan(multiple=False)
scan_session.scan.read()
image = scan_session.images[0]
pyinsane2.exit()
