import heapq

class IP_Address_Handler():

	# Initializer for the handler
	def __init__(self):
		# Hashtable/dictionary to store ip address as key and times called as value
		self.ip_dict = {}
		# A minimum heap to track the top 100 ip address
		self.min_heap = []

	# Calling function of each request, takes the ip address as input
	# Assuming all inputs are valid ip address
	def request_handled(self, ip_address:str):
		# Add the times if this ip has been called, otherwise add it into map with value 1
		if self.ip_dict.get(ip_address) == None:
			self.ip_dict[ip_address] = 1
		else:
			self.ip_dict[ip_address] += 1

	# Function that returns the top 100 ip addresses that are called most times
	def top100(self):
		# For each ip addresses, check the value and push it into the heap
		for ip in self.ip_dict.keys():
			heapq.heappush(self.min_heap,ip)
		# Return the 100 largest values in the heap
		return heapq.nlargest(100, self.min_heap)


	# Reset Function for renewing the tracking of ip addresses every day
	def clear(self):
		# Clear all the keys and values in the dictionary and values in the heap
		self.ip_dict.clear()
		self.min_heap = []
		
