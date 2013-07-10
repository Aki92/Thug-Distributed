import psutil
import redis
import time

class FindSendPerformance(object):
	def __init__(self):
		self.performance = 0
		self.make_connection()
		self.hostname = 'w1'
		
	# Finding performance of system using system config.
	def find_performance(self):
		nc = psutil.NUM_CPUS
		#bt = psutil.get_boot_time()
		cp = psutil.cpu_percent(interval = 1)
		fm = psutil.virtual_memory().free
		# Using simple formula: Num_Cpu*(Free_Memory(GB)*10)*(Free_Cpu/10)
		perf = nc * (fm/10**9)*10 * (100 - cp)/5
		self.performance = perf

	# Making connection to Redis Server 
	def make_connection(self):
		self.re = redis.StrictRedis(host='localhost', port=6379)
		
	# Sending performance to SORTED SET in Redis
	def send_value(self):
		# Adding performance value in SORTED SET(automatically sorts) in Redis
		amt = self.performance - self.re.zscore('perf',self.hostname)
		self.re.zincrby('perf', self.hostname, amt)
		
if __name__ == '__main__':
	fsp = FindSendPerformance()
	# Updating performance value after every 2 min.
	while True:
		fsp.find_performance()
		fsp.send_value()
		# Waiting for 2 min.
		time.sleep(60*2)
		