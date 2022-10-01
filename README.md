# Automatic Day Scheduler
My scheduler will take activities and start time of first task as input, and output the order and time to execute each task. The scheduler will use a priority queue, implemented by a maxheap, to store the tasks and tasks with greater priority will be executed first. Priority value is calculated based on the custom utility function. 

## Sample Output
<img width="768" alt="Screen Shot 2022-10-01 at 7 04 23 PM" src="https://user-images.githubusercontent.com/49523649/193430005-49028969-342f-43e7-a413-832b37dd882f.png">


## Data Structure
The priority queue is a suitable data structure to handle the prioritization of tasks because each tasks would have a priority attributes that represents its priority and higher priority items would be executed first. Its main advatage is that any operations of priority queue, like insert or update key, takes O(lgn) time for a queue of size n, making modifying and maintaining the data structure highly efficient. This is because it is based on a heap structure and traversing through the heap takes O(lgn).

## Advantages
The main benefit of this task scheduler is that it automatically produced a schedule that reflected your preferences and mostly followed constraints of reality. The task schedular reflected your preferences in that the activities are scheduled based on priority, which is calculated using a utility function whose weight you assigned. Moreover, the task schedular followed reality's constraint by implementing dependencies, which only allows some tasks to be performed after a certain task is performed, such that it will not produce an illogical schedule(e.g., have breakfast before fring eggs).

## Limitations
One major limitation is the implementation of start time. Some tasks have a very strict start time (such as meetings), and they will not be executed before a certain time. The task scheduler implemented start time by assigning it highest priority if the start time is reached, but did not restrict it performing before the start time, which is problematic for some activities. Another limitation is that the input it requires is complex, which might take more time to create the input than the user would like.
