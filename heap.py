# arr = [1, 4, 3, 7, 8, 9, 10,0,2,100,100]
# arr[(i-1)/2]	Returns the parent node
# arr[(2*i)+1]	Returns the left child node
# arr[(2*i)+2]	Returns the right child node

import math


class MinHeapQueue(object):
    def __init__(self):
        self.heap_queue = []
        self.last_index = -1
        self.left = None
        self.right = None

    def push(self, data):
        self.heap_queue.append(data)
        self.last_index += 1
        self.__bubble_up(data=data, index=self.last_index)

    def pop(self):
        if not self.heap_queue:
            raise None
        else:
            self.heap_queue[0] = self.heap_queue[self.last_index]
            self.heap_queue=self.heap_queue[:len(self.heap_queue)-1]
            self.last_index -= 1
            self.__bubble_down()


    def get(self):
        return self.heap_queue

    def __bubble_up(self, data, index):
        parent_index = (index - 1) // 2
        if parent_index >= 0:
            parent_value = self.heap_queue[parent_index]
            if parent_value > data:
                self.__swap(index, parent_index)
                self.__bubble_up(data, parent_index)

    def __bubble_down(self):
        index = 0
        while index <= self.last_index // 2:
            left_index = (2 * index) + 1
            right_index = (2 * index) + 2
            if left_index <= index and right_index <= index:
                if self.heap_queue[index] > self.heap_queue[left_index]:
                    self.__swap(index, left_index)
            index += 1

    def __swap(self, source, destination):
        self.heap_queue[source], self.heap_queue[destination] = \
            self.heap_queue[destination], self.heap_queue[source]


if __name__ == '__main__':
    min_heap_queue = MinHeapQueue()
    min_heap_queue.push(10)
    min_heap_queue.push(4)
    min_heap_queue.push(15)
    min_heap_queue.pop()
    min_heap_queue.push(20)
    min_heap_queue.push(0)
    min_heap_queue.push(30)
    min_heap_queue.pop()
    min_heap_queue.pop()
    min_heap_queue.push(0)
    min_heap_queue.push(-1)
    min_heap_queue.push(100)
    min_heap_queue.push(-1)
    min_heap_queue.push(-2)
    print(min_heap_queue.get())

