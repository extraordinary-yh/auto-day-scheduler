#!/usr/bin/env python
# coding: utf-8

class MaxHeap:
    """ 
    A class that implements properties and methods 
    that support a max priority queue data structure

    Attributes
    ----------
    heap : arr
       A Python list where key values in the max heap are stored
    heap_size: int
        An integer counter of the number of keys present in the max heap
    """  

    def __init__(self,heap):    
        """
        Parameters
        ----------
        heap: arr
            A Python list where we want to implement max-heap on.
        """    
        self.heap       = heap
        self.heap_size  = len(heap)
        
    def left(self, i):
        """
        Takes the index of the parent node
        and returns the index of the left child node
        
        Returns
        ----------
        int
            Index of the right child node
        """

        return 2 * i + 1
    
    def right(self, i):
        """
        Takes the index of the parent node
        and returns the index of the right child node
        
        Parameters
        ----------
        i: int
            Index of parent node

        Returns
        ----------
        int
            Index of the right child node

        """

        return 2 * i + 2

    def parent(self, i):
        """
        Takes the index of the child node
        and returns the index of the parent node
        
        Parameters
        ----------
        i: int
            Index of child node

        Returns
        ----------
        int
            Index of the parent node
         """

        return (i - 1)//2

    def maxkey(self):     
        """
        Returns the highest key in the priority queue. 
        
        Parameters
        ----------
        None

        Returns
        ----------
        int
            the highest key in the priority queue

        """
        return self.heap[0]     
    
  
    def heappush(self, task):  
        """
        Insert a task into a priority queue 
        
        Parameters
        ----------
        task: Task object
            The task to be inserted

        Returns
        ----------
        None
        """
        #create a dummyTask that has the lowest priority(-1)
        dummyTask = Task2(-1, "dummy task", 0, [], -1)
        self.heap.append(dummyTask)
        self.increase_key(self.heap_size,task)
        self.heap_size+=1
        
    def increase_key(self, i, task): 
        """
        Modifies the priority of a task in a max priority queue
        with a higher value
        
        Parameters
        ----------
        i: int
            The index of the task to be modified
        task: Task object
            The new task with a new priority value

        Returns
        ----------
        None
        """
        #check if the current task have higher priority
        if task < self.heap[i]:
            raise ValueError('new task piority is smaller than the current task priority')
        self.heap[i] = task
        #maintain max-heap structure
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            j = self.parent(i)
            holder = self.heap[j]
            self.heap[j] = self.heap[i]
            self.heap[i] = holder
            i = j    
            
       
    def heapify(self, i):
        """
        Creates a max heap from the index given
        
        Parameters
        ----------
        i: int
            The index of the root node of the subtree to be heapify

        Returns
        ----------
        None
        """
        l = self.left(i)
        r = self.right(i)
        heap = self.heap
        #find largest priority task
        if l <= (self.heap_size-1) and heap[l] > heap[i]:
            largest = l
        else:
            largest = i
        if r <= (self.heap_size-1) and heap[r] > heap[largest]:
            largest = r
        #if largest priority task is not parent the node
        if largest != i:
            heap[i], heap[largest] = heap[largest], heap[i]
            self.heapify(largest)

    def heappop(self):
        """
        returns the highest priority task in the max priority queue
        and remove it from the max priority queue
        
        Parameters
        ----------
        None

        Returns
        ----------
        maxTask
            the task with highest priority in the heap that is extracted
        """
        #check if task exist
        if self.heap_size < 1:
            raise ValueError('Heap underflow: There are no keys in the priority queue ')
        maxTask = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heap_size-=1
        self.heapify(0)
        return maxTask


