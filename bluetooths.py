# bluetooths.py
import bluetooth

def detect_bluetooth_devices():
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, lookup_class=True)
    for addr, name, _ in nearby_devices:
        print(f"Bluetooth Device: {name} ({addr})")
