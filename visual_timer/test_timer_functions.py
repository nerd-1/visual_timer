
import pytest

import timer_functions.py
# TODO: Update function calls

class Test_check_input(object):
	def test_check_input_returns_true_with_correct_format(self):
		# TODO: Call 'check_input' and make sure it returns 'true' with the time format 'HH:MM:SS' 
		pass
	def test_check_input_returns_false_with_empty_string(self):
		# TODO: Call 'check_input' and make sure it returns 'false' with an empty string 
		pass
	def test_check_input_returns_false_with_wrong_string(self):
		# TODO: Call 'check_input' and make sure it returns 'false' with the string 'foobar' 
		pass

def test_divide_y_returns_the_correct_result():
	# TODO: Call 'divide_y' and make sure it returns '0.5' where 'timer_set' is 120 and 'y_dim' is 60
	result = func.divide_y(120, 60)
	assert result == 0.5

class Test_render_y(object):
	# TODO: Create test functions
	pass

class Test_format_seconds(object):
	# TODO: Create test functions
	pass

class Test_convert_to_sec(object):
	# TODO: Create test functions
	pass
		