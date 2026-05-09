class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def insert(self, root, key):

        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)

        else:
            root.right = self.insert(root.right, key)

        return root

    def inorder(self, root):

        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def search(self, root, key):

        if root is None or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)

tree = BST()

root = None

root = tree.insert(root, 50)
root = tree.insert(root, 30)
root = tree.insert(root, 70)

print("Inorder Traversal:")
tree.inorder(root)

print("\nSearch 30:", tree.search(root, 30))