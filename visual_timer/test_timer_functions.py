
import math
import time
import sys
import os
import re
import curses

import pytest

import timer_functions

class Test_check_input(object):
	def test_check_input_returns_true_with_correct_format(self):
		# TODO: Call 'check_input' and make sure it returns 'true' with the time format 'HH:MM:SS' 
		result = timer_functions.check_input("00:00:05")
		assert result == True
	def test_check_input_returns_false_with_empty_string(self):
		# TODO: Call 'check_input' and make sure it returns 'false' with an empty string 
		result = timer_functions.check_input("")
		assert result == False
	def test_check_input_returns_false_with_wrong_string(self):
		# TODO: Call 'check_input' and make sure it returns 'false' with the string 'foobar' 
		result = timer_functions.check_input("foobar")
		assert result == False

def test_divide_y_returns_the_correct_result():
	# TODO: Call 'divide_y' and make sure it returns '0.5' where 'timer_set' is 120 and 'y_dim' is 60
	result = timer_functions.divide_y(120, 60)
	assert result == 0.5

'''
# Giving up on this as it's too much work for very little benifit
# https://stackoverflow.com/questions/90002/what-is-a-reasonable-code-coverage-for-unit-tests-and-why?rq=1
class Test_render_y(object):
	def test_render_y_returns_empty_screen(self):
		
		#define variables here
		timer_set = 60				#What the timer was originally set to
		seconds_remaining = None	#Used exclusivly as a local variable in the "format_seconds" function. Useless
		formated_time = None
		y_dim = 64					#height of screen
		x_dim = 64					#width of screen

		with timer_functions.curses_stdscr() as stdscr:
			stdscr = curses.initscr()
			stdscr.nodelay(1)
			y_sec_unit = timer_functions.divide_y(timer_set, dimensions[0])
			stdscr = timer_functions.render_y(seconds, y_sec_unit, y_pixel_count, stdscr, x_dim, y_dim)

			pass


	def test_render_y_returns_full_screen(self):
		pass
	def test_render_y_returns_screen_with_top_three_rows_white(self):
		pass
'''

class Test_format_seconds(object):
	# TODO: Create test functions
	def test_format_seconds_seconds(self):
		seconds = 0
		timer_set = 2
		result = timer_functions.format_seconds(seconds, timer_set)
		assert result == "2"
	def test_format_seconds_minutes(self):
		seconds = 0
		timer_set = 122
		result = timer_functions.format_seconds(seconds, timer_set)
		assert result == "2m 2s"
	def test_format_seconds_hours(self):
		seconds = 0
		timer_set = 7322
		result = timer_functions.format_seconds(seconds, timer_set)
		assert result == "2h 2m 2s"
	def test_format_seconds_days(self):
		seconds = 0
		timer_set = 180122
		result = timer_functions.format_seconds(seconds, timer_set)
		assert result == "2d 2h 2m 2s"
	def test_format_seconds_years(self):
		seconds = 0
		timer_set = 63295322
		result = timer_functions.format_seconds(seconds, timer_set)
		assert result == "2y 2d 2h 2m 2s"
	def test_format_seconds_zero(self):
		pass
	pass

class Test_convert_to_sec(object):
	# TODO: Create test functions
	pass
		