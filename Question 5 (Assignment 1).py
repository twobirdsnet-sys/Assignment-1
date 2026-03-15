class SmartDevice:
    def __init__(self, name):
        self.name = name

    def reset(self):
        print(f"{self.name} device is resetting to factory settings.")


class SmartLight(SmartDevice):

    def reset(self):
        print(f"{self.name} light is resetting brightness and color settings.")


def reset_all_devices(devices_list):
    for device in devices_list:
        device.reset()


device1 = SmartDevice("Speaker")
device2 = SmartLight("Bedroom")
device3 = SmartDevice("Thermostat")
device4 = SmartLight("Kitchen")

devices = [device1, device2, device3, device4]

reset_all_devices(devices)
