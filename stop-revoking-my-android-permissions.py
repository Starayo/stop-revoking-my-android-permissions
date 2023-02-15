from ppadb.client import Client as ADBClient

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    client = ADBClient(host="127.0.0.1", port=5037)
    devices = client.devices()

    for device in devices:
        device_name = device.shell("settings get secure android_id")
        lines = device.shell("pm list packages").splitlines()
        lines = [string[8:] for string in lines]

        for line in lines:
            device.shell("appops set %s AUTO_REVOKE_PERMISSIONS_IF_UNUSED ignore" % line.strip())
            device.shell("appops --uid %s AUTO_REVOKE_PERMISSIONS_IF_UNUSED ignore" % line.strip())
            print("Device %s: set permission for %s" % (device_name.strip(), line.strip()))

    input("Operation complete. Press enter to exit.")
