# stop-revoking-my-android-permissions
A very simple python 3 script to stop android 11+ from revoking all my damn permissions when I don't use an app for a while.

The script grabs any android devices connected to ABD, grabs their list of packages, then iterates through them, setting AUTO_REVOKE_PERMISSIONS_IF_UNUSED to ignore for all apps.

### **Note that android does this for legitimate security reasons. I personally vet my own apps and am comfortable with the risk. Use at your own discretion.**

Uses pure-python-adb to interface with ADB. Install it with 
```pip install pure-python-adb```
or use the included requirements.txt file with
```pip install -r requirements.txt```

Also requires you to have ADB.

By default the script uses a USB connection to ADB. If you want to use it wirelessly, you can edit the host IP and port on line 5, but I haven't tested it.
