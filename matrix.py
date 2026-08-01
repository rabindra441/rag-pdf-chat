import curses
import random
import time

def draw_matrix(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    max_y, max_x = stdscr.getmaxyx()
    columns = [random.randint(0, max_y) for _ in range(max_x)]
    chars = "0123456789012345678901234567890123456701010101010101010101010101010101010101010101010110101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010\()"
    tail_length = 12


    while True:
        # stdscr.erase()
        for i, row in enumerate(columns):
            for t in range(tail_length):
                tail_row = row - t
                if 0 < tail_row < max_y:
                    char = random.choice(chars)
                    try:
                        stdscr.addstr(columns[i], i, char, curses.color_pair(1))
                    except:
                        curses.error
                pass
            if columns[i] > max_y - 1 or random.random() > 0.95:
                columns[i] = 0
            else:
                columns[i] += 1

        stdscr.refresh()
        time.sleep(0.10)

curses.wrapper(draw_matrix)