class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [0] * capacity
        self.capacity = capacity
        self.length = 0

    # Return i-th index. O(1)
    def get(self, i: int) -> int:
        return self.array[i]

    # Set i-th element to n
    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    # Push element to end of array. Resize array if full.
    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.array[self.length] = n
        self.length += 1

    # Pop and return element at the end of array
    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1

        return self.array[self.length]
 
    # Double capacity of array
    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_array = [0] * self.capacity

        # Copy elements to new_array
        for i in range(self.length):
            new_array[i] = self.array[i]

        self.array = new_array

    # Return number of elements in array
    def getSize(self) -> int:
        return self.length
        
    # return capacity of array
    def getCapacity(self) -> int:
        return self.capacity
