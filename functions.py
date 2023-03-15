import subprocess
import re

# to check
def find_ssid_name():
    profile_info_interface = subprocess.run(["netsh", "wlan", "show", "interface"], capture_output = True).stdout.decode()
    print(profile_info_interface)
    # ssid = re.findall("SSID            : (.*)\r", profile_info_interface)
    # # wifi_ssid_name = ssid[0]
    # # print(wifi_ssid_name)
    # print(ssid)



#Second function To find SSID password
def find_wifi_password(name):
    profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
    password = re.findall("Key Content            : (.*)\r", profile_info_pass)
    wifi_pass = password[0]
    print(wifi_pass)


name = find_ssid_name()
find_wifi_password(name)
# find_wifi_password('''bennun''')