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
        last_value = self.arr[self.length - 1]
        
        # overwrite value and decrement length
        self.arr[self.length - 1] = None
        self.length -= 1

        return last_value
 
    # double capacity of array
    def resize(self) -> None:
        old_cap = self.capacity
        # double current capacity
        self.capacity = self.capacity * 2
        # copy old arr into new array
        new_arr = [None] * self.capacity
        for i in range(old_cap):
            new_arr[i] = self.arr[i]
        # overwrite old arr
        self.arr = new_arr

    # return array length
    def getSize(self) -> int:
        return self.length
        
    # return capacity
    def getCapacity(self) -> int:
        return self.capacity
