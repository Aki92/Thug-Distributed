import netifaces as nf
import subprocess

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
		# Finding both IP4 & IP6 addresses
		network_interfaces = nf.interfaces()
		# Keeping only connections other than ethernet, wireless, localhost
		network_interfaces = [n for n in network_interfaces if(not
							  n.startswith('lo') and not n.startswith('eth') and
							  not n.startswith('wlan'))
							  ]
		ip4 = ''
		ip6 = ''
		for network in network_interfaces:
			# Finding IP4 address
			try:
				ip4 = nf.ifaddresses(network)[nf.AF_INET][0]['addr']
			except:
				pass

			# Finding IP6 address
			try:
				ip6 = nf.ifaddresses(network)[nf.AF_INET6][0]['addr']
			except:
				pass

		self.ip4 = ip4
		self.ip6 = ip6
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
		# Try-Except used because check_output raises error if command doesn't
		# run successfully
		try:
			if(self.ip4_req != ""):
				dns = subprocess.check_output("dig +short %s.%s TXT" %
											(self.ip4_req, self.ip4_server),
											shell=True
											)
				if dns != '':
					country = dns.split(" | ")[2]
			elif(self.ip6_req != ""):
				dns = subprocess.check_output("dig +short %s.%s TXT" %
											(self.ip6_req, self.ip6_server),
											shell=True
											)
				if dns != '':
					country = dns.split(" | ")[2]
		except:
			country = ""
			
		self.country = country
		return self.country