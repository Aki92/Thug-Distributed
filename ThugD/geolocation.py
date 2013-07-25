from urllib2 import urlopen
from config import site
import dns.resolver
import json

"""
This Class is first finding both IP4 & IP6 addresses using "netifaces"
library. Then it is finding the location of user by using the TEAM CYMRU
service corresponding the IP address found.
"""
class FindLocation(object):
    def __init__(self):
        # Common IP4 & IP6 variables
        self.ip4 = ''
        self.ip6 = ''
        # Server addresses of TEAM CYMRU
        self.ip4_server = "origin.asn.cymru.com"
        self.IP6_server = "origin6.asn.cymru.com"

    def find_ip(self):
        ip = ''
        # Finding IP address from site
        try:
            content = urlopen(site).read()
            ip = str(json.loads(content)['YourFuckingIPAddress'])
        except:
            print '** Please Check your Internet Connection and URL provided **'
        
        # Checking if returned ip address is IP4 or IP6
        if ip != '':
            if ip.count('.') == 3:
                self.ip4 = ip
            else:
                self.ip6 = ip
                
        return (self.ip4, self.ip6)

    def modify_ip4(self, ip4):
        if(ip4 != ''):
            # Splitting on "." then reversing the list and joining with "."
            ip4_addresses = ip4.split(".")
            ip4_addresses.reverse()
            ip4 = ".".join(ip4_addresses)
            
        self.ip4_req = ip4

    def modify_ip6(self, ip6):
        if(ip6 != ''):
            # Removing address part after "::"
            ip6 = ip6.split("::")[0]
            # Reversing the address
            ip6 = ip6[::-1]
            # Removing all ":"
            ip6_addresses = ip6.replace(":", "")
            # Making required changes to pass in DNS Query for geolocation
            ip6 = ".".join(list(ip6_addresses))

        self.ip6_req = ip6
        
    def find_country(self):
        # Running required functions to find country name
        self.find_ip()
        self.modify_ip4(self.ip4)
        self.modify_ip6(self.ip6)
        country = ''
        # Finding country using team cymru and dnspython library
        try:
            obj = None
            if(self.ip4_req != ""):
                obj = dns.resolver.query("dig +short %s.%s" % 
                                            (self.ip4_req, self.ip4_server), 
                                            'TXT')
            elif(self.ip6_req != ""):
                obj = dns.resolver.query("dig +short %s.%s" % 
                                            (self.ip6_req, self.ip6_server),
                                            'TXT')
            # Traversing the dns object
            if obj is not None:				
                for info in obj:
                    if info != '':
                        country = str(info).split(" | ")[2]
        except:
            pass
                
        self.country = country
        return self.country

if __name__ == '__main__':
    loc = FindLocation()
    print loc.find_country()