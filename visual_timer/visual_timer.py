
import timer_functions

import math
import time
import sys
import os
import re
import curses

timer_set = 60
seconds = 0
seconds_remaining = None
formated_time = None
curses.curs_set(0)

# Check for empty strings #
try:
	time_str = str(sys.argv[1])
except:
	timer_functions.output_help()
	sys.exit()

# Check for invalid strings #
if timer_functions.check_input(time_str) == False:
	timer_functions.output_help()
	sys.exit()

# Main #
with timer_functions.curses_stdscr() as stdscr:
	timer_set = timer_functions.convert_to_sec(time_str)
	stdscr = curses.initscr()
	stdscr.nodelay(1)
	dimensions = stdscr.getmaxyx()
	y_dim = int(dimensions[0])
	x_dim = int(dimensions[1])
	y_pixel_count = 0
	x_pixel_count = 0

	while seconds <= timer_set:
		dimensions = stdscr.getmaxyx()
		y_dim = int(dimensions[0])
		x_dim = int(dimensions[1])
		stdscr.clear()
		y_sec_unit = timer_functions.divide_y(timer_set, dimensions[0])
		stdscr = timer_functions.render_y(seconds, y_sec_unit, y_pixel_count, stdscr, x_dim, y_dim)
		stdscr, formated_time = timer_functions.render_time(seconds, stdscr, y_dim, x_dim, formated_time, timer_set)
		stdscr.refresh()
		y_pixel_count += y_sec_unit
		seconds += 1
		time.sleep(1)
