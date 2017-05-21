#!/usr/bin/env pythonfrom os import system
import datetime
import curses

def pretty_time_delta(delta_time):
    if delta_time == None:
        return "-"
    seconds = delta_time.total_seconds()
    sign_string = '-' if seconds < 0 else ''
    seconds = abs(int(seconds))
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    if days > 0:
        return '%s%dd%dh%dm%ds' % (sign_string, days, hours, minutes, seconds)
    elif hours > 0:
        return '%s%dh%dm%ds' % (sign_string, hours, minutes, seconds)
    elif minutes > 0:
        return '%s%dm%ds' % (sign_string, minutes, seconds)
    else:
        return '%s%ds' % (sign_string, seconds)

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
    def newTask(title):
        global history
        history.append(History('New task'))
        new_task = Task(title)
        tasks.append(new_task) # add new task to the master list 
        return new_task

    @staticmethod
    def setContinue(id):
        global active_task_id
        global history
        history.append(History('Task continued'))
        selected_task = tasks[id]
        selected_task.setLastContinue()
        active_task_id = selected_task.id

    @staticmethod
    def setPaused():
        global active_task_id
        global history
        history.append(History('Task paused'))
        selected_task = tasks[active_task_id]
        selected_task.setPaused()
        active_task_id = -1

class History:
    def __init__(self,action_name):
        self.action_name = action_name
        self.date = datetime.datetime.now()

class Task:
    'Common base class for all tasks'
    comment = ''
    last_continue = None
    total_time = None

    def __init__(self, title="default_title"):
        global last_id
        if (title == ""):
            self.title = "default_title"
        else:
            self.title = title
        self.id = last_id+1
        last_id+=1
        self.created_at = datetime.datetime.now()

    def setLastContinue(self):
        self.last_continue = datetime.datetime.now()

    def setPaused(self):
        elapsed_time = datetime.datetime.now() - self.last_continue
        if (self.total_time == None):
            self.total_time = elapsed_time
        else:
            self.total_time += elapsed_time

def view_task(offset_y, offset_x, task):
    screen.addstr(offset_y,offset_x,str(task.id))
    screen.addstr(offset_y,offset_x+5,str(task.title))
    screen.addstr(offset_y,offset_x + 30,pretty_time_delta(task.total_time))
    # screen.addstr(offset_y,offset_x + 50,str(task.comment))

def view_history(offset_y, offset_x, history):
    screen.addstr(offset_y,offset_x,str(history.action_name))
    screen.addstr(offset_y,offset_x + 30,str(history.date))

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
active_task_id = -1
last_id = -1
selected_option = 0

Actions.newTask("hello world 1")
Actions.newTask("hello world 2")
Actions.newTask("hello world 3")

while selected_option != ord('4'):
    screen = curses.initscr()

    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, "Please enter a number...")
    screen.addstr(4, 4, "1 - n e w")
    continue_pause_view = "p a u s e" if (active_task_id > 0) else "c o n t i n u e"
    screen.addstr(5, 4, "2 - "+continue_pause_view)
    screen.addstr(6, 4, "3 - h i s t o r y")
    screen.addstr(7, 4, "4 - e x i t ")

    if (active_task_id >= 0):
        active_task = tasks[active_task_id]

        screen.addstr(10, 4, "Currently Active: ")
        screen.addstr(11,4,str(active_task.id))
        screen.addstr(11,6,str(active_task.title))
        # screen.addstr(11,30,str(task.total_time))

        screen.addstr(10, 30, "Elapsed time: ")
        elapsed_time = datetime.datetime.now() - active_task.last_continue
        pretty_elapsed_time = pretty_time_delta(elapsed_time)
        screen.addstr(11,30,str(pretty_elapsed_time))

        screen.addstr(10, 49, "Total time: ")
        screen.addstr(11,49,str(pretty_time_delta(active_task.total_time)))
        # screen.addstr(11,90,str(active_task.total_time))
    else:
        screen.addstr(10, 4, "No task currently active.")

    screen.addstr(13, 4, "= = = = T A S K S = = = =")
    screen.addstr(14, 6, "_id_")
    screen.addstr(14, 12, "_title_")
    screen.addstr(14, 36, "_time_")
    view_tasks(15,5)

    screen.refresh()
    selected_option = screen.getch()

    if selected_option == ord('1'):
        screen.addstr(2, 2, "                                        ")
        screen.addstr(2, 2, "Please enter the new session name...")
        screen.addstr(4, 15, "                   >_ ")
        screen.refresh()
        input = screen.getstr(4, 35, 60)

        Actions.newTask(input)
        # view_tasks_index(); # show me the list of tasks

    if selected_option == ord('2'):
        if (active_task_id >= 0):
            Actions.setPaused()

        else:
            # pause one of the tasks
            screen.addstr(2, 2, "                                        ")
            screen.addstr(2, 2, "Please enter the task to continue...")
            screen.addstr(5, 25, "             >_ ")
            screen.refresh()
            input = screen.getstr(5, 40, 60)
            try:
                Actions.setContinue(int(input))
            except:
                pass
    if selected_option == ord('3'):
        view_history_index();

curses.endwin()

