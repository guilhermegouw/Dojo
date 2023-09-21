class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def remove(self):
        if self.items:
            return self.items.pop(0)
        return 'Empty queue'
    
    def peek(self):
        if self.items:
            return self.items[0]
        return 'Empty queue'
    

class Deque:
    def __init__(self):
        self.items = []
    
    def push_front(self, item):
        self.items.insert(item, 0)
    
    def push_back(self, item):
        self.items.append(item)
    
    def remove_front(self):
        if self.items:
            return self.items.pop(0)
        return 'Empty deque'
    
    def remove_back(self):
        if self.items:
            return self.items.pop()
        return 'Empty deque'
    
    def peek_front(self):
        if self.items:
            return self.items[0]
        return 'Empty deque'
    
    def peek_back(self):
        if self.items:
            return self.items[-1]
        return 'Empty deque'
