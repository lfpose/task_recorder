#!/usr/bin/env pythonfrom os import system
import datetime
import curses

def show_last_create(offset_x, offset_y):
    screen.addstr(offset_y, offset_x, "Last sessions created")
    screen.addstr(offset_y+1, offset_x, "------------------")
    for i in range(0,5): 
        screen.addstr(offset_y + i,offset_x+2,str(tasks[i]))

def view_history_index():
    screen.clear()
    screen.addstr(0,0,'Command history')
    screen.addstr(3,10,'Select: ')
    screen.addstr(5,3,'== H I S T O R Y ==')
    offset_y = 7
    offset_x = 4
    for i in range(0,len(history)): 
        view_history(offset_y+i,offset_x+2,history[i])
    screen.refresh()
    screen.getstr(3, 20, 60)


def view_tasks(offset_y, offset_x):
    global tasks
    for i in range(0,len(tasks)): 
        view_task(offset_y+i,offset_x+2,tasks[i])

def view_tasks_index():
    global tasks
    screen.clear()
    screen.border(0)
    screen.addstr(0,0,'List of tasks')
    screen.addstr(3,10,'Search: ')
    screen.addstr(5,3,'== T A S K S ==')
    offset_y = 7
    offset_x = 4
    for i in range(0,len(tasks)): 
        view_task(offset_y+i,offset_x+2,tasks[i])
    screen.refresh()
    screen.getstr(3, 20, 60)

class Actions():
    @staticmethod
    def new_task(title):
        global history
        history.append(History('New task'))
        new_task = Task(title)
        tasks.append(new_task) # add new task to the master list 
        return new_task

class History:
    def __init__(self,action_name):
        self.action_name = action_name
        self.date = datetime.datetime.now()

class Task:
    'Common base class for all tasks'
    comment = ''

    def __init__(self, title="default_title"):
        global last_id
        if (title == ""):
            self.title = "default_title"
        else:
            self.title = title
        self.id = last_id+1
        last_id+=1
        self.created_at = datetime.datetime.now()


def view_task(offset_y, offset_x, task):
    screen.addstr(offset_y,offset_x,str(task.id)+":")
    screen.addstr(offset_y,offset_x+5,str(task.title))
    screen.addstr(offset_y,offset_x + 10,str(task.comment))

def view_history(offset_y, offset_x, history):
    screen.addstr(offset_y,offset_x,str(history.action_name))
    screen.addstr(offset_y,offset_x + 10,str(history.date))

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
history = []
active_task = -1
last_id = -1
selected_option = 0

Actions.new_task("hello world 1")
Actions.new_task("hello world 2")
Actions.new_task("hello world 3")

while selected_option != ord('4'):
    screen = curses.initscr()

    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, "Please enter a number...")
    screen.addstr(4, 4, "1 - n e w")
    screen.addstr(5, 4, "2 - c o n t i n u e")
    screen.addstr(6, 4, "3 - h i s t o r y")
    screen.addstr(7, 4, "4 - e x i t ")

    if (active_task >= 0):
        screen.addstr(10, 4, "Currently Active: ")
        view_task(11,10,tasks[active_task])
    else:
        screen.addstr(10, 4, "No task currently active.")
    screen.refresh()

    screen.addstr(12, 4, "List of tasks")
    view_tasks(13,4)

    selected_option = screen.getch()

    if selected_option == ord('1'):
        screen.addstr(2, 2, "                                        ")
        screen.addstr(2, 2, "Please enter the new session name...")
        screen.addstr(4, 15, "                   >_ ")
        screen.refresh()
        input = screen.getstr(4, 35, 60)

        Actions.new_task(input)
        # view_tasks_index(); # show me the list of tasks

    if selected_option == ord('2'):
        screen.addstr(2, 2, "                                        ")
        screen.addstr(2, 2, "Please enter the task to continue...")
        screen.addstr(5, 25, "             >_ ")
        screen.refresh()
        input = screen.getstr(5, 40, 60)
        try:
            selected_task = tasks[int(input)]
            active_task = selected_task.id
            Actions.set_continue(id)
        except:
            pass
    if selected_option == ord('3'):
        view_history_index();

curses.endwin()

