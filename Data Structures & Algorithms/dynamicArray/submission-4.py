class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [None] * capacity

    # get element at i-th index
    def get(self, i: int) -> int:
        return self.arr[i]

    # set element at i-th index
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    # push element to end of array
    def pushback(self, n: int) -> None:
        # resize if at capacity
        if self.capacity == self.length:
            self.resize()
            
        # push element to next open spot
        self.arr[self.length] = n
        self.length += 1

    # pop and return element at end of array
    def popback(self) -> int:
        if self.length > 0:
            # soft delete the last element
            self.length -= 1
        # return the popped element
        return self.arr[self.length]
 
    # double capacity of array
    def resize(self) -> None:
        # double current capacity
        self.capacity = self.capacity * 2
        new_arr = [None] * self.capacity

        # copy elements into new array
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.length
        
    def getCapacity(self) -> int:
        return self.capacity
