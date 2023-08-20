import pymem
import re
from time import sleep
dg = False
while not dg:
    try:
        pm = pymem.Pymem('csgo.exe')
        pm.close_process()
        dg = True
    except:
        pass
pm = pymem.Pymem('csgo.exe')
client = pymem.process.module_from_name(pm.process_handle, 'client.dll')
clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
walladdress = client.lpBaseOfDll + re.search(rb'\x33\xC0\x83\xFA.\xB9\x20', clientModule).start() + 4
radaraddress = client.lpBaseOfDll + re.search(rb'\x74\x15\x8B\x47\x08\x8D\x4F\x08', clientModule).start() - 1
moneyaddress = client.lpBaseOfDll + re.search(rb'.\x0C\x5B\x5F\xB8\xFB\xFF\xFF\xFF', clientModule).start()
duckaddress = client.lpBaseOfDll + re.search(rb'\x81\xE2.{4}\x84\xDB', clientModule).start() + 4
while True:
    try:
        if pm.read_uchar(walladdress) == 0:
            print("Wall Hack detected.")
        if pm.read_uchar(radaraddress) == 2:
            print("Radar Hack detected.")
        if pm.read_uchar(moneyaddress) == 0xEB:
            print("Money Hack detected.")
        if pm.read_uchar(duckaddress) == 0x42:
            print("Quick Duck Hack detected.")
    except:
        print("Game closed.")
    sleep(10)
