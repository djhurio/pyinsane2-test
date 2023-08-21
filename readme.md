Vispārīgi par:
<https://chat.openai.com/share/3c38c732-d0e8-4de7-b900-a295a5159c35>

Te ir kods pārbaudei:
<https://gitlab.gnome.org/World/OpenPaperwork/pyinsane/-/tree/master/>

Papildus vajadzēja pievienot `pyinsane2.init()`:

```
import pyinsane2

pyinsane2.init()
try:
	devices = pyinsane2.get_devices()
	assert(len(devices) > 0)
	device = devices[0]

	print("I'm going to use the following scanner: %s" % (str(device)))
	scanner_id = device.name
finally:
	pyinsane2.exit()
```

Uz Windows būs problēma ar SANE instalāciju:
<https://stackoverflow.com/questions/9278263/is-it-possible-to-use-the-sane-backend-on-windows-platforms>
