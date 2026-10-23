class MinStack:

    def __init__(self):
        self.array = []
        self.prefix = []
        
    def push(self, val: int) -> None:
        if not len(self.array):
            self.prefix.append(val)
        elif val < self.prefix[len(self.array) - 1]:
            self.prefix.append(val)
        else:
            self.prefix.append(self.prefix[len(self.array) - 1])
        self.array.append(val)

    def pop(self) -> None:
        self.array.pop()
        self.prefix.pop()
        
    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.prefix[len(self.array) - 1]