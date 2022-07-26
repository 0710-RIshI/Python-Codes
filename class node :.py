


class BinarySearchTree :
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self,data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)
    
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    
def build_tree(elements):
        root = BinarySearchTree(elements)

        for i in range(1,len(elements)):
            root.add_child(elements[i])
        return root

if __name__ == '__main__':
    number = [17,4,6,7,2,2,23]
    number_tree = build_tree(number)
    print(number_tree.in_order_traversal())
    
