class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        val = self.arr[self.size]
        self.set(self.size, 0)
        return val

    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [0] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

["Array", 4, "pushback", 1, "set", 0, 0, "pushback", 2, "get", 0, "get", 1, "getCapacity", "popback"]

def main():
    initCapacity = 4

    arr = DynamicArray(initCapacity)
    arr.pushback(1)
    arr.set(0,0)
    arr.pushback(2)
    print(arr.get(0))
    print(arr.get(1))
    print(arr.getCapacity())
    print(arr.popback())



if __name__ == "__main__":
    main()
