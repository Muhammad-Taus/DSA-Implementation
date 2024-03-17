class MyArray:
    def __init__(self):
        self.length = 0
        self.data = []

    def get(self, index):
        if 0 <= index < self.length:
            return self.data[index]
        return None
    
    def find(self, item):
        for i in range(self.length):
            if self.data[i] == item:
                return i
        return -1

    def push(self, item):
        self.data.append(item)
        self.length += 1

    def insert(self, index, item):
        """
        Inserts an item at the specified index in the array.
        Time complexity: O(n), where n is the number of elements in the array.
        """
        if not (0 <= index <= self.length):
            return None
        self.shift_items(index)
        self.data.insert(index, item)
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        last_item = self.data.pop()
        self.length -= 1
        return last_item

    def delete(self, index):
        if not (0 <= index < self.length):
            return None
        deleted_item = self.data.pop(index)
        self.length -= 1
        return deleted_item


    def shift_items(self, index):
        """
        Shifts the items in the array to the right, starting from the specified index.
        """
        for i in range(self.length - 1, index - 1, -1):
            self.data.append(self.data[i])
        self.length += 1

    def print_array(self):
        """
        Prints the current state of the array.
        """
        print(self.data)

# Example usage
my_array = MyArray()

my_array.push("apple")
my_array.push("banana")
my_array.push("orange")

my_array.insert(1, "grapes")
print(my_array.data)  # Output: ['apple', 'grapes', 'banana', 'orange']
