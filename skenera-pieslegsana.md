## Skenera pieslēgšana Python
### 1. Pakotnes
- 1.1. pyinsane2 
    ```
    import pyinsane2
    devices = pyinsane2.get_devices()
    print(devices) # prints the list of scanners
    scanner = devices[0] # selects the first scanner
    scan_session = scanner.scan(multiple=False) # starts a single scan
    ```
    Python nenolasa skeneri, kaut PC to redz.
    Vienāds error no darba un privātā PC.

    Mārtiņš L. pārbauda pieslēgt savu skeneri.

- 1.2. python-sane 
    Neizdodas uzstādīt ne no darba, ne privātā datora. Nevar izveidot pakotnes wheel.

### 2. Skeneris
Skeneris ir Canon LiDE220.
Pilnu banknoti nav iespējams noskenēt globālu nosacījumu dēļ.
Jānoskaidro vai NAP ir citas tiesības.
