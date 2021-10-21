class Node(object):
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous


class LinkList(object):
    def __init__(self, data=None):
        node = None
        if data is not None:
            node = Node(data)
        self.head = node

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = node.previous = None
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            else:
                current_node.next = node
                node.next = None
                node.previous = current_node

    def to_string(self):
        result = '['
        current_node = self.head
        while current_node.next:
            result += str(current_node.data) + ","
            current_node = current_node.next
        else:
            result += str(current_node.data) + "]"
        return result

    def get_node(self, index):
        __index = 0
        current_node = self.head
        while current_node:
            if __index == index:
                return current_node.data
            current_node = current_node.next
            __index += 1
        raise IndexError("Index out of bound error.")

    def pop(self, index=None):
        if index is None:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            else:
                current_node.previous.next = None
                del current_node
        else:
            if index == 0:
                self.head = self.head.next
                self.head.previous = None
                return
            __index = 0
            current_node = self.head
            while current_node.next:
                if __index == index:
                    current_node.previous.next = current_node.next
                    current_node.next.previous = current_node.previous
                    return
                __index += 1
                current_node = current_node.next
            else:
                if __index == index:
                    current_node.previous.next = None
                    return
                raise IndexError("Index out of bound error.")

    def push(self, index, data):
        node = Node(data)
        if index == 0:
            node = Node(data)
            node.next = self.head
            self.head.previous = node
            self.head = node
            return
        __index = 0
        current_node = self.head
        while current_node.next:
            if __index == index:
                current_node.previous.next = node
                node.next = current_node
                current_node.previous = node
                node.previous = current_node.previous
                return
            current_node = current_node.next
            __index += 1
        else:
            if index == __index:
                current_node.next = node
                node.previous = current_node
                return
        raise IndexError("Index out of bound error.")

    def is_exist(self, data):
        cnt = 0
        current_node = self.head
        while current_node.next:
            if current_node.data == data:
                cnt += 1
            current_node = current_node.next
        if cnt > 0:
            return True, cnt
        return False


link_list = LinkList(0)
link_list.append(1)
link_list.append(2)
link_list.append(3)
link_list.append(4)
print(link_list.to_string())
print(link_list.get_node(2))
# link_list.pop(4)
link_list.push(4, 10)
print(link_list.to_string())
print(link_list.is_exist(10))
print(link_list.to_string())

