class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity 
        
        self.storage = [None]*capacity
        self.current = 0 

    def append(self, item):
        self.storage[self.current] = item
        if self.current + 1 < self.capacity:
            self.current += 1
        else:
            self.current = 0

    def get(self):
        my_list = []
        for i in self.storage:
            if i :
                my_list.append(i)
        return my_list