
import math
import time
import sys
import os
import re
import curses

seconds = 0

def is_even(number):
	if (number%2 == 0):
		return('even')
	return('odd')

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

def check_input(time_str):
	if re.match("[0-9][0-9]:[0-9][0-9]:[0-9][0-9]", time_str) != None:
		return(True)
	else:
		return(False)

def output_help():
	os.chdir("..")
	os.chdir("docs")
	file = open("usage.txt", "r")
	file_out = file.read()
	print(file_out)
	file.close

def divide_y(timer_set, y_dim):
	#Divides the hight of screen by the set time (in secconds)
	y_sec_unit = y_dim/timer_set
	return(y_sec_unit)

def render_y(seconds, y_sec_unit, y_pixel_count, stdscr, x_dim, y_dim):
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
	return(stdscr)

def render_time(seconds, stdscr, y_dim, x_dim, formated_time, timer_set):
	formated_time = format_seconds(seconds, timer_set)
	stdscr.addstr(math.ceil(((y_dim)-1)/2), math.ceil((x_dim-len(formated_time))/2), formated_time, curses.A_BOLD)
	return(stdscr, formated_time)

def format_seconds(seconds, timer_set, hide_seconds=False):
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
