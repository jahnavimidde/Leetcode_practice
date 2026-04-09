class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val):
        self.stack.append(val)
        
        # Push into minstack if empty OR val <= current min
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)

    def pop(self):
        # If popped element is min, pop from minstack also
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minstack[-1]