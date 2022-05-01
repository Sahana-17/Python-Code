# Test code - HEALTH MONITORING SYSTEM
# Created by : Sahana Muralikrishnan

# While I followed a TDD process while writing my source code, I didn't push them as individual commits. 
# Each time I wrote a new function, I stubbed it, then tested for failure and then amended to allow for success.

import pytest
from src.health_system import average_pulse, abnormal_pulse


class TestClass:
	# failure - all negative inputs
	def test_average_pulse_negative_input(self):
		assert(average_pulse(-13,-14,-20) == None)

		# failure for single negative input
		assert(average_pulse(-60,70,80) == None)	

	# success - all positive pulse values
	def test_average_pulse(self):
		assert(average_pulse(60,70,80) == 70)	

	#failire for pulse below min_value
	def test_min_abnormal_pulse(self):
		assert(abnormal_pulse(40,75,86,68) == 1)

	#failure for pulse above max_value
	def test_max_abnormal_pulse(self):
		assert(abnormal_pulse(65,77,100,88) == 3)

	#success - all normal pulse values
	def test_abnormal_pulse(self): 
		assert(abnormal_pulse(66,77,88,89) == None)
	
	#success - boundary values 60(min) and 90(max) are also accepted
	def test_boundary_abnormal_pulse(self):
		assert(abnormal_pulse(60,70,80,90) == None)
