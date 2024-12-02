import turtle
import random
from collections import deque
import keyboard

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class BSTree:
    def __init__(self):
        self.root = None

    def insertBestCase(self, key):
        key = sorted(key)
        self.root = self._buildBalancedTree(key)

    def insertWorstCase(self, key):
        for value in key:
            self.insert(value)

    def insertAvCase(self, key):
        random.shuffle(key)
        for value in key:
            self.insert(value)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insertRecursive(self.root, key)

    def _insertRecursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insertRecursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insertRecursive(node.right, key)

    def _buildBalancedTree(self, key):
        if not key:
            return None
        mid = len(key) // 2
        root = Node(key[mid])
        root.left = self._buildBalancedTree(key[:mid])
        root.right = self._buildBalancedTree(key[mid + 1:])
        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.root = self._deleteRecursive(self.root, key)

    def _deleteRecursive(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._deleteRecursive(node.left, key)
        elif key > node.key:
            node.right = self._deleteRecursive(node.right, key)
        else:

            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_larger_node = self._findMin(node.right)
            node.key = min_larger_node.key

            node.right = self._deleteRecursive(node.right, min_larger_node.key)

        return node

    def _findMin(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self, key):
        result = []
        self._inorderCollect(key, result)
        return " ".join(map(str, result))


    def preorder(self, key):
        result = []
        self._preorderCollect(key, result)
        return " ".join(map(str, result))


    def postorder(self, key):
        result = []
        self._postorderCollect(key, result)
        return " ".join(map(str, result))


    def levelOrder(self):
        if self.root is None:
            return ""
        queue = deque([self.root])
        result = []
        while queue:
            node = queue.popleft()
            result.append(str(node.key))
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return " ".join(result)


    def _inorderCollect(self, node, result):
        if node:
            self._inorderCollect(node.left, result)
            result.append(node.key)
            self._inorderCollect(node.right, result)

    def _preorderCollect(self, node, result):
        if node:
            result.append(node.key)
            self._preorderCollect(node.left, result)
            self._preorderCollect(node.right, result)

    def _postorderCollect(self, node, result):
        if node:
            self._postorderCollect(node.left, result)
            self._postorderCollect(node.right, result)
            result.append(node.key)

    def getHeight(self):
        return self._getHeight(self.root)

    def _getHeight(self, node):
        if node is None:
            return 0
        left_height = self._getHeight(node.left)
        right_height = self._getHeight(node.right)
        return max(left_height, right_height) + 1

    def drawTree(self):
        turtle.clear()
        turtle.speed(100)
        turtle.hideturtle()
        self._drawTree(self.root)
        while True:
            if keyboard.is_pressed('Enter'):
                break

    def _drawTree(self,node, x=0, y=200, dx=150, dy=50, radius=20):
        if node is None:
            return

        self.drawNode(x, y, radius, node.key)

        if node.left:
            child_x = x - dx
            child_y = y - dy
            turtle.penup()
            turtle.goto(x, y - radius)
            turtle.pendown()
            turtle.goto(child_x, child_y + radius)
            self._drawTree(node.left, child_x, child_y, dx / 2, dy, radius)

        if node.right:
            child_x = x + dx
            child_y = y - dy
            turtle.penup()
            turtle.goto(x, y - radius)
            turtle.pendown()
            turtle.goto(child_x, child_y + radius)
            self._drawTree(node.right, child_x, child_y, dx / 2, dy, radius)

    def drawNode(self, x, y, radius, label):
        turtle.penup()
        turtle.goto(x, y - radius)
        turtle.pendown()
        turtle.circle(radius)
        turtle.penup()
        turtle.goto(x, y - radius)
        turtle.write(label, align="center", font=("Arial", 12, "normal"))














