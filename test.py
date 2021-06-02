import pytest
from IP_Address_Handler_Songbo import IP_Address_Handler

IP_Handler = IP_Address_Handler()

IP_Handler.request_handled("145.87.2.109")
IP_Handler.request_handled("145.87.2.110")
IP_Handler.request_handled("145.87.2.109")
IP_Handler.request_handled("145.87.2.111")
IP_Handler.request_handled("145.87.2.110")
IP_Handler.request_handled("145.87.2.109")

def test_top100():
	assert IP_Handler.top100() == ["145.87.2.109","145.87.2.110","145.87.2.111"]

def test_clear():
	IP_Handler.clear()
	assert IP_Handler.min_heap == None and IP_Handler.ip_dict == None
