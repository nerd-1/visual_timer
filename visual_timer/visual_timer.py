
'''
    Timer Part finished
'''

import curses
import math
import time
import sys, getopt

timer_set = 60
seconds = 0
time_str = str(sys.argv[1])

#def set_time(argv):
#	try:
#		opts, args = getopt.getopt(argv,"t:",["time="])
#	except getopt.GetoptError:
#		print ('timer.py -t <time>')
#		sys.exit(2)
#	for opt, arg in opts:
#		if opt in ("-t", "--time"):
#			timer_set = arg

class curses_stdscr:
    def __enter__(self):
        self.stdscr = curses.initscr()
        curses.cbreak()
        curses.noecho()
        self.stdscr.keypad(1)
        stdscr_HEIGHT, stdscr_WIDTH = self.stdscr.getmaxyx()
        return self.stdscr
    def __exit__(self,a,b,c):
        curses.nocbreak()
        self.stdscr.keypad(0)
        curses.echo()
        curses.endwin()

def divide_y(timer_set, y_dim):
	
	y_sec_unit = y_dim/timer_set
	return(y_sec_unit)

def render_y(seconds, y_sec_unit, y_pixel_count):
	cursor_y = 0
	cursor_x = 0
	for sec_unit in range(int(y_pixel_count)):
		try:
			while (cursor_x < x_dim) and (cursor_y < y_dim):
				stdscr.addch(cursor_y, cursor_x, "█")
				cursor_x += 1
		except:
			pass
		cursor_y += 1
		cursor_x = 0
	return()

def render_time(seconds):
	formated_time = format_seconds(seconds)
	stdscr.addstr(math.ceil(((y_dim)-1)/2), math.ceil((x_dim-len(formated_time))/2), formated_time, curses.A_BOLD)
	return()

def format_seconds(seconds, hide_seconds=False):
    #This function was taken from the termdown project and was written by trehn
    seconds_remaining = timer_set - seconds
    if seconds_remaining <= 60:
        return str(seconds_remaining)
    output = ""
    for period, period_seconds in (
        ('y', 31557600),
        ('d', 86400),
        ('h', 3600),
        ('m', 60),
        ('s', 1),
    ):
        if seconds_remaining >= period_seconds and not (hide_seconds and period == 's'):
            output += str(int(seconds_remaining / period_seconds))
            output += period
            output += " "
            seconds_remaining = seconds_remaining % period_seconds
    return output.strip()

def convert_to_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

#if __name__ == '__main__':
with curses_stdscr() as stdscr:
	timer_set = convert_to_sec(time_str)
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
		y_sec_unit = divide_y(timer_set, dimensions[0])
		render_y(seconds, y_sec_unit, y_pixel_count)
		render_time(seconds)
		stdscr.refresh()
		y_pixel_count += y_sec_unit
		seconds += 1
		time.sleep(1)
	

'''
    Timer Part finished
'''

import curses
import math
import time
import sys, getopt

timer_set = 60
seconds = 0
time_str = str(sys.argv[1])

#def set_time(argv):
#	try:
#		opts, args = getopt.getopt(argv,"t:",["time="])
#	except getopt.GetoptError:
#		print ('timer.py -t <time>')
#		sys.exit(2)
#	for opt, arg in opts:
#		if opt in ("-t", "--time"):
#			timer_set = arg

class curses_stdscr:
    def __enter__(self):
        self.stdscr = curses.initscr()
        curses.cbreak()
        curses.noecho()
        self.stdscr.keypad(1)
        stdscr_HEIGHT, stdscr_WIDTH = self.stdscr.getmaxyx()
        return self.stdscr
    def __exit__(self,a,b,c):
        curses.nocbreak()
        self.stdscr.keypad(0)
        curses.echo()
        curses.endwin()

def divide_y(timer_set, y_dim):
	
	y_sec_unit = y_dim/timer_set
	return(y_sec_unit)

def render_y(seconds, y_sec_unit, y_pixel_count):
	cursor_y = 0
	cursor_x = 0
	for sec_unit in range(int(y_pixel_count)):
		try:
			while (cursor_x < x_dim) and (cursor_y < y_dim):
				stdscr.addch(cursor_y, cursor_x, "█")
				cursor_x += 1
		except:
			pass
		cursor_y += 1
		cursor_x = 0
	return()

def render_time(seconds):
	formated_time = format_seconds(seconds)
	stdscr.addstr(math.ceil(((y_dim)-1)/2), math.ceil((x_dim-len(formated_time))/2), formated_time, curses.A_BOLD)
	return()

def format_seconds(seconds, hide_seconds=False):
    #This function was taken from the termdown project and was written by trehn
    seconds_remaining = timer_set - seconds
    if seconds_remaining <= 60:
        return str(seconds_remaining)
    output = ""
    for period, period_seconds in (
        ('y', 31557600),
        ('d', 86400),
        ('h', 3600),
        ('m', 60),
        ('s', 1),
    ):
        if seconds_remaining >= period_seconds and not (hide_seconds and period == 's'):
            output += str(int(seconds_remaining / period_seconds))
            output += period
            output += " "
            seconds_remaining = seconds_remaining % period_seconds
    return output.strip()

def convert_to_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

with curses_stdscr() as stdscr:
	timer_set = convert_to_sec(time_str)
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
		y_sec_unit = divide_y(timer_set, dimensions[0])
		render_y(seconds, y_sec_unit, y_pixel_count)
		render_time(seconds)
		stdscr.refresh()
		y_pixel_count += y_sec_unit
		seconds += 1
		time.sleep(1)
	
#if __name__ == '__main__':
