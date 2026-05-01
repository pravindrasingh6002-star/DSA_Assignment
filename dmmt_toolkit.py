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

    def search(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def min_value(self, node):
        while node.left:
            node = node.left
        return node

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            
            if root.left is None and root.right is None:
                return None
           
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            
            temp = self.min_value(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, w))

    def show(self):
        print("\nAdjacency List:")
        for node in self.graph:
            print(node, "->", self.graph[node])

    def bfs(self, start):
        visited = set()
        queue = [start]

        print("\nBFS:", end=" ")
        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                for n, _ in self.graph.get(node, []):
                    if n not in visited:
                        queue.append(n)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
            print("\nDFS:", end=" ")

        print(start, end=" ")
        visited.add(start)

        for n, _ in self.graph.get(start, []):
            if n not in visited:
                self.dfs(n, visited)


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return key % self.size

    def insert(self, key, value):
        i = self.hash(key)
        self.table[i].append((key, value))

    def get(self, key):
        i = self.hash(key)
        for k, v in self.table[i]:
            if k == key:
                return v
        return None

    def delete(self, key):
        i = self.hash(key)
        for index, (k, v) in enumerate(self.table[i]):
            if k == key:
                del self.table[i][index]
                return True
        return False

    def show(self):
        print("\nHash Table:")
        for i, bucket in enumerate(self.table):
            print(i, "->", bucket)


def main():
    print("===== BST =====")
    bst = BST()
    root = None

    for i in [50,30,70,20,40,60,80]:
        root = bst.insert(root, i)

    print("Inorder:", end=" ")
    bst.inorder(root)

    print("\nSearch 20:", bst.search(root,20))
    print("Search 90:", bst.search(root,90))

    root = bst.delete(root,20)
    print("\nAfter deleting 20:", end=" ")
    bst.inorder(root)

    root = bst.insert(root,65)
    root = bst.delete(root,60)
    print("\nAfter deleting 60:", end=" ")
    bst.inorder(root)

    root = bst.delete(root,30)
    print("\nAfter deleting 30:", end=" ")
    bst.inorder(root)

    print("\n\n===== GRAPH =====")
    g = Graph()

    edges = [
        ('A','B',2),('A','C',4),('B','D',7),
        ('B','E',3),('C','E',1),('D','F',5),
        ('E','D',2),('E','F',6),('C','F',8)
    ]

    for u,v,w in edges:
        g.add_edge(u,v,w)

    g.show()
    g.bfs('A')
    g.dfs('A')

    print("\n\n===== HASH TABLE =====")
    h = HashTable(5)

    for k in [10,15,20,7,12]:
        h.insert(k,k*10)

    h.show()

    print("\nGet 10:", h.get(10))
    print("Get 15:", h.get(15))
    print("Get 7:", h.get(7))

    h.delete(15)
    print("\nAfter deleting 15:")
    h.show()


if __name__ == "__main__":
    main()