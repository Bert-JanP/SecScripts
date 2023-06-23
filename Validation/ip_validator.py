import re

def ip_validator(ip_address):
    regex_validator = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    if(re.search(regex_validator, ip_address)):
        return True
    else:
        print('IP address: %s is not valid.' %ip_address)
        return False 