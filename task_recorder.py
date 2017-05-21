#!/usr/bin/env python
from os import system
import curses

def get_param(prompt_string):
    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, prompt_string)
    screen.refresh()
    input = screen.getstr(10, 10, 60)
    return input

def debuger():
    global tasks
    screen.clear()
    screen.border(0)
    screen.addstr(0,0,'Debugger')
    screen.addstr(5,3,'== T A S K S ==')
    offset_v = 7
    offset_x = 4
    for i in range(1,len(tasks)): 
        screen.addstr(offset_v + i,offset_x,'*')
        screen.addstr(offset_v + i,offset_x+2,str(tasks[i]))
    screen.refresh()
    input = screen.getstr(10, 10, 60)
    return input

def create_task():
    global last_id

    new_id = last_id + 1
    default_task = {
            'id': new_id ,
            'name': 'default_name', 
            'comments': ''
            }
    last_id = new_id
    return default_task

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



tasks = [] # {id: 1, name: 'task_recorder', 'comments':''}
active_task_id = -1
last_id = -1
selected_option = 0



while selected_option != ord('4'):
    screen = curses.initscr()

    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, "Please enter a number...")
    screen.addstr(4, 4, "1 - n e w")
    screen.addstr(5, 4, "2 - c o n t i n u e")
    screen.addstr(6, 4, "3 - h i s t o r y")
    screen.addstr(7, 4, "4 - e x i t ")
    screen.refresh()

    selected_option = screen.getch()

    if selected_option == ord('1'):
        screen.addstr(10, 10, "[ >_ option ' n e w ' selected ]")
        title = get_param("Enter the session name:")
        screen.addstr(2, 2, "Please enter a number...")
        new_task = create_task()
        #new_task.name = title
        tasks.append(new_task)

        debuger();
    if selected_option == ord('2'):
        screen.addstr(10, 10, "[ >_ option ' c o n t i n u e ' selected ]")
    if selected_option == ord('3'):
        screen.addstr(10, 10, "[ >_ option ' h i s t o r y ' selected ]")

curses.endwin()

