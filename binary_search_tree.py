class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while 1:
                if current_node.data == data:
                    return
                else:
                    if data > current_node.data:
                        if current_node.right is None:
                            current_node.right = node
                            return
                        else:
                            current_node = current_node.right
                    else:
                        if current_node.left is None:
                            current_node.left = node
                            return
                        else:
                            current_node = current_node.left

    def find(self, data):
        current_node = self.root
        while current_node:
            if data == current_node.data:
                return current_node
            if data > current_node.data:
                current_node = current_node.right
            elif data < current_node.data:
                current_node = current_node.left
        return None

    def remove(self, data):
        current_node = self.root
        is_right = False
        parent = None
        while current_node:
            if data == current_node.data:
                # Leaf Node Removal
                if current_node.left is None \
                        and current_node.right is None:
                    if is_right:
                        parent.right = None
                    else:
                        parent.left = None
                    return True
                # node having either left or right subtree
                if current_node.left is None or current_node.right is None:
                    if is_right:
                        parent.right = current_node.right
                    else:
                        parent.left = current_node.left
                    return True
                # node having both left and right sub-tree
                if current_node.left and current_node.right:
                    right_node = current_node.right
                    left_node = right_node
                    while left_node:
                        if left_node.left:
                            left_node = left_node.left
                        else:
                            break
                    left_node_data = left_node.data
                    self.remove(left_node.data)
                    current_node.data = left_node_data
                    return True

            if data > current_node.data:
                is_right = True
                parent = current_node
                current_node = current_node.right

            elif data < current_node.data:
                is_right = False
                parent = current_node
                current_node = current_node.left
        return False

    def pre_order(self, node):
        if node:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)
        else:
            return

    def in_order(self, node):
        if node:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
        else:
            return

    def post_order(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)
        else:
            return

    @staticmethod
    def level_order(node):
        queue = [node]
        while queue:
            node = queue.pop(0)
            print(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


bst = BinarySearchTree()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(7)
bst.insert(0)
bst.insert(4)
bst.insert(14)
bst.insert(12)
bst.insert(9)

node = bst.find(8)
if node:
    bst.level_order(node)
