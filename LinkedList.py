class Node(object):
    def __init__(self, data, node=None):
        self.data = data
        self.next_node = node


class LinkedList(object):
    def __init__(self, root=None):
        self.root = root

    def add_node(self, data):
        new_node = Node(data=data, node=self.root)
        self.root = new_node

    def delete_node(self, data):
        current_node = self.root
        pre_node = None
        while current_node is not None:
            if current_node.data == data:
                if pre_node is not None:
                    pre_node.next_node = current_node.next_node
                else:
                    self.root = current_node.next_node

                return True
            else:
                pre_node = current_node
                current_node = current_node.next_node

        return False

    def traverse(self):
        linked_list_item = self.root
        while linked_list_item is not None:
            print(linked_list_item.data)
            linked_list_item = linked_list_item.next_node


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add_node(5)
    linked_list.add_node(6)
    linked_list.add_node(7)
    linked_list.add_node(8)
    linked_list.add_node(9)
    print("Traverse Before Delet")
    linked_list.traverse()
    linked_list.delete_node(7)
    print("Traverse After Delete")
    linked_list.traverse()
