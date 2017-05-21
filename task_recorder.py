#!/usr/bin/env python
from os import system
import curses

# def get_param(prompt_string):
    # screen.clear()
    # screen.border(0)
    # screen.addstr(2, 2, prompt_string)
    # screen.refresh()
    # input = screen.getstr(10, 10, 60)
    # return input

# def execute_cmd(cmd_string):
    # system("clear")
    # a = system(cmd_string)
    # print ""
    # if a == 0:
        # print "Command executed correctly"
    # else:
        # print "Command terminated with error"
    # raw_input("Press enter")
    # print ""



x = 0
while x != ord('4'):
    screen = curses.initscr()

    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, "Please enter a number...")
    screen.addstr(4, 4, "1 - n e w")
    screen.addstr(5, 4, "2 - c o n t i n u e")
    screen.addstr(6, 4, "3 - h i s t o r y")
    screen.addstr(7, 4, "4 - e x i t ")
    screen.refresh()

    x = screen.getch()

    if x == ord('1'):
        screen.addstr(10, 10, "[ >_ option ' n e w ' selected ]")
        title = get_param("Enter the session name:")

        # execute_cmd("useradd -d " + homedir + " -g 1000 -G " + groups + " -m -s " + shell + " " + username)
    if x == ord('2'):
        screen.addstr(10, 10, "[ >_ option ' c o n t i n u e ' selected ]")
    if x == ord('3'):
        screen.addstr(10, 10, "[ >_ option ' h i s t o r y ' selected ]")

curses.endwin()
