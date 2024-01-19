class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add(self, data):
        new_node = Node(data)
        self.children.append(new_node)

    def remove(self, data):
        self.children = [child for child in self.children if child.data != data]


class Tree:
    def __init__(self):
        self.root = None

    def traverseBF(self, fn):
        if not self.root:
            return

        queue = [self.root]
        while queue:
            current = queue.pop(0)
            fn(current)
            queue.extend(current.children)

    def traverseDF(self, fn):
        if not self.root:
            return

        stack = [self.root]
        while stack:
            current = stack.pop()
            fn(current)
            stack.extend(reversed(current.children))


# Przykład użycia
def print_node(node):
    print(node.data)

tree = Tree()
tree.root = Node(1)
tree.root.add(2)
tree.root.add(3)
tree.root.children[0].add(4)
tree.root.children[0].add(5)

print("Breadth-First Traversal:")
tree.traverseBF(print_node)

print("\nDepth-First Traversal:")
tree.traverseDF(print_node)
