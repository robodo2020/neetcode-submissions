class MinStack:

    def __init__(self):
        """
        stack: cur append value
        minstack: cur min value in the stack
        [1,2,0,-3,1,2]
        [1,1,0,-3,-3,-3]
        """
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            self.minstack.append(min(val, self.minstack[-1]))
        else:
            self.minstack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minstack[-1]
        
