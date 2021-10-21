class Node():
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            else:
                current_node.next_node = Node(data)

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def display(self):
        current_node = self.head
        while (current_node):
            print(current_node.data)
            current_node = current_node.next_node

    def delete(self, position):
        current_node = self.head
        if position == 0:
            self.head = self.head.next_node
        else:
            cnt = 1
            while current_node.next_node:
                if position == cnt:
                    current_node.next_node = current_node.next_node.next_node
                    break
                current_node=current_node.next_node
                cnt += 1


linked_list = LinkedList(Node(1))
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.delete(3)
linked_list.display()
