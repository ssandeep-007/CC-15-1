class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.idx = 0 
    def build_tree(self, arr):
        if self.idx >= len(arr):
            return None

        if arr[self.idx] == -1:
            self.idx+=1
            return None

        root = Node(arr[self.idx])
        self.idx += 1
        root.left = self.build_tree(arr)
        root.right = self.build_tree(arr)

        return root

    def is_bst(self, root, min_val, max_val):
        if root is None:
            return True

        if root.data <= min_val or root.data >= max_val:
            return False

        return (self.is_bst(root.left, min_val, root.data) and
                self.is_bst(root.right, root.data, max_val))


arr = list(map(int, input().split()))
bst = BST()
root = bst.build_tree(arr)

result = bst.is_bst(root, float('-inf'), float('inf'))
print(result)









