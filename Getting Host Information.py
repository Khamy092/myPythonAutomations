

import socket
import platform
import os
import requests

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("www.facebook.com", 80))
    return s.getsockname()[0]

hostname = socket.gethostname()
os_details = platform.uname() 
isp = socket.gethostbyaddr(get_ip_address())[0]
location = requests.get('http://ipinfo.io/json').json()


# write to file and put a line break after each line 
with open('output.txt', 'w') as f:
    f.write('Hostname: ' + hostname + '\r')
    f.write('OS: ' + os_details[0] + ' ' + os_details[2] + '\r')
    f.write('ISP: ' + isp + '\r')
    f.write('Location: ' + location['city'] + ', ' + location['region'] + '\r')
    f.write('IP: ' + get_ip_address() + '\r')
    f.write('Public IP: ' + location['ip'] + '\r')
    f.write('Country: ' + location['country'] + '\r')
    f.write('Timezone: ' + location['timezone'] + '\r')
    f.write('Coordinates: ' + location['loc'] + '\r')
    f.write('Organization: ' + location['org'] + '\r')
    f.write('Postal: ' + location['postal'] + '\r')
    f.write('Hostname: ' + location['hostname'] + '\r')
    f.write('Bogon: ' + str(location['bogon']) + '\r')

# close the file
f.close()

