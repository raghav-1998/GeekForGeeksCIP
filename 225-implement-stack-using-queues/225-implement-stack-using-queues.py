from queue import Queue
class MyStack:

    def __init__(self):
        self.q1=Queue()
        self.q2=Queue()
        self.curr_size=0

    def push(self, x: int) -> None:
        self.q1.put(x)
        self.curr_size+=1

    def pop(self) -> int:
        if (self.q1.empty()):
            return
        
        while(self.q1.qsize() != 1):
            self.q2.put(self.q1.get())
        
        popped = self.q1.get()
        self.curr_size -= 1
        
        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q
        
        return popped
    def top(self) -> int:
        if (self.q1.empty()):
            return
        
        while(self.q1.qsize() != 1):
            self.q2.put(self.q1.get())
        
        top = self.q1.queue[0]
        self.q2.put(self.q1.get())
        
        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q
        
        return top

    def empty(self) -> bool:
        return self.curr_size==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()