#!/usr/bin/env python3

import curses
from curses import wrapper
import time
import random

def startup(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test")
    stdscr.addstr("\nPress any Key to begin!")
    stdscr.refresh()
    stdscr.getkey()

def display(stdscr, target, current, wpm=0):
    stdscr.addstr(sample)
    stdscr.addstr(1, 0, f'WPM: {wpm}')

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color)

def load_text():
    with open("typing.txt") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def test(stdscr):
    sample = load_text()
    current = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display(stdscr, sample, current)
        stdscr.refresh()

        if "".join(current) == sample:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current) > 0:
                current.pop()
        elif len(current) < len(sample):
            current.append(key)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    startup(stdscr)
    while True:
        test(stdscr)

        stdscr.addstr(2, 0, "You have completed the test! Press any key to continue . . .")
        stdscr.getkey()
        if ord(key) == 27:
            break

wrapper(main)
