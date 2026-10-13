class DynamicArray:
    
    def __init__(self, capacity: int):
        # instantiate arr
        self.arr = [None] * capacity
        # set capacity
        self.capacity = capacity
        # set length = 0
        self.length = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        # set idx to n
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # if at capacity, resize
        if self.capacity == self.length:
            self.resize()
        # add value to next available spot
        self.arr[self.length] = n
        # increment length
        self.length += 1

    def popback(self) -> int:
        last_idx = self.length - 1
        last_value = self.arr[last_idx]
        # overwrite last element
        self.arr[last_idx] = None
        # decrement length
        self.length -= 1
        # return value
        return last_value

    def resize(self) -> None:
        old_capacity = self.capacity
        # double capacity
        self.capacity = old_capacity * 2
        # create new arr
        new_arr = [None] * self.capacity
        # copy old_arr to new_arr
        for i in range(old_capacity):
            new_arr[i] = self.arr[i]
        # replace old arr
        self.arr = new_arr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity