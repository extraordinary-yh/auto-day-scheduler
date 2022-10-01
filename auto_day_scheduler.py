#!/usr/bin/env python
# coding: utf-8


class Task2:
    """
    A class that implements activity objects with multitasking feature

    Attributes
    ----------
    - id: Task Id   
    - description: Short description of the task   
    - duration: Duration in minutes   
    - dependencies: list of dependencies it's going to focus on
    - dimentions: a list of 0s and 1s to store a task's value dimentions as well as strict starttime
    - priority: priority level of a task (ranging from 0 to 10)  
    - multitask: a boolean value that indicate whether a task can be multitasked with other tasks
    - status: Current status of the task 
   
    """
    #Initializes an instance of Task
    def __init__(self,task_id,description,duration,dependencies,valueDimentions = [0,0,0,0,0],  multitask = False, priority = 0, status="N"):
        self.id= task_id
        self.description=description
        self.duration=duration
        self.dependencies=dependencies
        self.valueDimention = valueDimentions
        self.status=status
        self.priority=priority
        self.multitask = multitask
    
    def updatePriority(self, curTime):
        #if task's start time equals current time
        if self.valueDimention[0] <= curTime and self.valueDimention[0] != 0:
            self.priority = 10
        else:
            self.priority = self.valueDimention[1]*3 + self.valueDimention[2]*2 + self.valueDimention[3]*3 + self.valueDimention[4]*1
        
    def __repr__(self):
        return f"{self.description} - id: {self.id}\n \tDuration:{self.duration}\n\tDepends on: {self.dependencies}\n\tStatus: {self.status}"

    def __gt__(self, other):
        return self.priority > other.priority
    
    def __lt__(self, other):
        return self.priority < other.priority
    
class TaskScheduler:
    """
    A Simple Daily Task Scheduler Using Priority Queues
    
    Attributes
    ----------
    - tasks: a list object that stores the tasks to be scheduled
    - priority_queue: the priority_queue to store the task
    - myHeap: a MaxHeap object to access the heap functions
    
    """
    NOT_STARTED ='N'
    IN_PRIORITY_QUEUE = 'I'
    COMPLETED = 'C'
    
    def __init__(self, tasks):
        self.tasks = tasks
        self.priority_queue = []
        self.myHeap = MaxHeap(self.priority_queue)
        
    def print_self(self):
        print('Input List of Tasks')
        for t in self.tasks:
            print(t)            
            
    def remove_dependency(self, task_id):
        """
        Input: list of tasks and task_id of the task just completed
        Output: lists of tasks with t_id removed
        """
        for t in self.tasks:
            if t.id != task_id and task_id in t.dependencies:
                t.dependencies.remove(task_id)           
            
    def get_tasks_ready(self,curTime):
        """ 
        Implements step 1 of the scheduler
        Input: list of tasks, the current time
        Output: list of tasks that are ready to execute (i.e. tasks with no pendending task dependencies)
        """
        for task in self.tasks:
            task.updatePriority(curTime)
            #Check if task is in queue and has dependencies
            if task.status == self.NOT_STARTED and not task.dependencies: 
                # Change status of the task
                task.status = self.IN_PRIORITY_QUEUE 
                # Push task into the priority queue
                self.myHeap.heappush(task)
    
    def check_unscheduled_tasks(self):
        """
        Input: list of tasks 
        Output: boolean (checks the status of all tasks and returns True if at least one task has status = 'N'
        """
        for task in tasks:
            if task.status == self.NOT_STARTED:
                return True
        return False   
    
    def get_multitask(self):
        """
        Input: list of tasks 
        Output: boolean value, returns whether a task that can multitask and can fulfill the requirement is found
        """
        #loop through item in priority_queue (all of which have not started and don't have dependencies )
        for i in range(len(self.priority_queue)):
            task = self.priority_queue[i] 
            #if another task that support multitask is found
            if task.multitask:
                #give it highest priority of all task 
                task.priority = 11
                self.myHeap.heapify(i)
                return True
        return False
    
    def update_duration(self,task1,task2):
        """
        Input: two tasks
        Output: the total duration of completing two tasks together, the shorter task and the longer task
        """
        if task1.duration >= task2.duration:
            total_duration = task1.duration
            task1.duration -= task2.duration
            return total_duration, task2, task1
        else:
            total_duration = task2.duration
            task2.duration -= task1.duration
            return total_duration, task1, task2
    
    def format_time(self, time):
        return f"{time//60}h{time%60:02d}"
    
    def run_task_scheduler(self, starting_time = 480):
        current_time = starting_time
        while self.check_unscheduled_tasks() or self.priority_queue:
            #extract tasks ready to execute (those without dependencies) and push them into the priority queue
            self.get_tasks_ready(current_time)
            #check for tasks in the priority queue. 
            if len(self.priority_queue) > 0 :  
                task = self.myHeap.heappop()
                #check for multitask ability
                if task.multitask and self.get_multitask():
                    task2 = self.myHeap.heappop()
                    total_duration, first_task, second_task = self.update_duration(task, task2) 
                    print(f"⏰Simple Scheduler at time {self.format_time(current_time)} started multitasking task {first_task.id} and task {second_task.id} that takes in total {total_duration} mins")
                    #execute first task
                    current_time += first_task.duration            
                    print(f"✅ Completed Task {first_task.id} - '{first_task.description}' of priority '{first_task.priority}' at time {self.format_time(current_time)}") 
                    #remove completed task from the dependency list
                    self.remove_dependency(first_task.id)
                    first_task.status = self.COMPLETED
                    #execute second task
                    current_time += second_task.duration            
                    print(f"✅ Completed Task {second_task.id} - '{second_task.description}' of priority '{second_task.priority}' at time {self.format_time(current_time)}\n") 
                    #remove completed task from the dependency list
                    self.remove_dependency(second_task.id)
                    second_task.status = self.COMPLETED
                #if no multi-task
                else:
                    print(f"⏰Simple Scheduler at time {self.format_time(current_time)} started executing task {task.id} that takes {task.duration} mins")
                    current_time += task.duration            
                    print(f"✅ Completed Task {task.id} - '{task.description}' of priority '{task.priority}' at time {self.format_time(current_time)}\n") 
                    #remove completed task from the dependency list
                    self.remove_dependency(task.id)
                    task.status = self.COMPLETED
        total_time = current_time - starting_time             
        print(f"🏁 Completed all planned tasks in {total_time//60}h{total_time%60:02d}min")


# In[8]:


'''
Test Cases

tasks = [
    Task2(0, 'get up at 8:00 AM', 10, [], [0,1,1,1,1],True), 
    Task2(1, 'get dressed and ready', 10, [0],[480,0,1,1,1]), 
    Task2(2, 'eat healthy breakfast', 40, [0],[600,1,1,0,1]), 
    Task2(3, 'make grocery list', 20, [0]), 
    Task2(4, 'go to the market', 15, [1, 3],[800,1,0,1,1]), 
    Task2(5, 'buy groceries in list', 30, [4],[1000,1,0,0,1]), 
    Task2(6, 'drive back home', 15, [],[500,0,0,0,0],True), 
    Task2(7, 'store groceries', 5, [6])]
'''

#real inputs
tasks = [Task2(1, 'fry eggs', 5, [], [0,0,0,0,0]),
    Task2(2, 'heat bread', 5, [], [0,0,0,0,0]),
    Task2(3, 'enjoy the breakfest', 10, [1,2], [520,0,1,0,1],True),
    Task2(4, 'research history', 30, [3], [0,1,0,0,0]),
    Task2(5, 'search bus route', 5, [3], [0,0,0,0,0]),
    Task2(6, 'visit seodaemun prison history hall', 180, [4,5], [600,1,0,0,1],True),
    Task2(7, 'invite friends', 10, [6], [0,1,0,0,0]),
    Task2(8, 'discuss preferences', 5, [7], [0,1,0,0,0],True),
    Task2(9, 'search for places', 10, [7], [0,0,0,0,0],True),
    Task2(10, 'enjoy the lunch', 60, [7,8,9], [0,0,1,1,1]),
    Task2(11, 'watch introductory videos', 10, [10], [0,1,0,0,0]),
    Task2(12, 'buy audio guidebook', 5, [10], [0,1,0,0,0]),
    Task2(13, 'take pictures', 60, [11,12], [0,0,0,0,1]),
    Task2(14, 'organize reflections', 20, [13], [0,1,0,0,0],True),
    Task2(15, 'charge my computer', 10, [13], [0,0,0,0,0],True),
    Task2(16, 'attend meeting', 60, [14,15], [1200,1,1,0,0])]

task_scheduler = TaskScheduler(tasks)
task_scheduler.run_task_scheduler()

