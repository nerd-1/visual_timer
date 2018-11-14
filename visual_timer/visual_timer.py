
import timer_functions

# TODO: Update function calls

# Check for empty strings #
try:
	time_str = str(sys.argv[1])
except:
	output_help()
	sys.exit()

# Check for invalid strings #
if check_input(time_str) == False:
	output_help()
	sys.exit()

# Main #
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
