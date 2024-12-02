import turtle
import keyboard

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return Node(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)


        node.height = 1 + max(self._getHeight(node.left), self._getHeight(node.right))


        balance = self.getBalance(node)


        if balance > 1:
            if key < node.left.key:
                return self.rightRotate(node)
            else:
                node.left = self.leftRotate(node.left)
                return self.rightRotate(node)
        elif balance < -1:
            if key > node.right.key:
                return self.leftRotate(node)
            else:
                node.right = self.rightRotate(node.right)
                return self.leftRotate(node)

        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return root

        elif key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)

        root.height = 1 + max(self._getHeight(root.left), self._getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        elif balance < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def search(self, key):
        return True if self._search(self.root, key) is not None else False

    def _search(self, root, key):
        if root is None:
            return None
        elif key < root.key:
            return self._search(root.left, key)
        elif key > root.key:
            return self._search(root.right, key)
        else:
            return root

    def inorder(self, root):
        if root is None:
            return []
        return self.inorder(root.left) + [root.key] + self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return []
        return [root.key] + self.preorder(root.left) + self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return []
        return self.postorder(root.left) + self.postorder(root.right) + [root.key]

    def levelOrder(self):
        if not self.root:
            return []
        queue = [self.root]
        result = []
        while queue:
            node = queue.pop(0)
            if node is not None:
                result.append(node.key)
                queue.append(node.left)
                queue.append(node.right)
        return result



    def getBalance(self, root):
        if not root:
            return 0
        return self._getHeight(root.left) - self._getHeight(root.right)

    def leftRotate(self, y):
        x = y.right
        T2 = x.left

        x.left = y
        y.right = T2

        y.height = 1 + max(self._getHeight(y.left), self._getHeight(y.right))
        x.height = 1 + max(self._getHeight(x.left), self._getHeight(x.right))

        return x

    def rightRotate(self, x):
        y = x.left
        T2 = y.right

        y.right = x
        x.left = T2

        x.height = 1 + max(self._getHeight(x.left), self._getHeight(x.right))
        y.height = 1 + max(self._getHeight(y.left), self._getHeight(y.right))

        return y
    def minValueNode(self, node):
        current = node
        while (current.left is not None):
            current = current.left
        return current

    def _getHeight(self, node):
        if not node:
            return 0
        return node.height

    def getHeight(self):
        if not self.root:
            return 0
        return self.root.height

    def _fillLevels(self, node, depth, levels):
        if depth == len(levels):
            levels.append([])

        if node:
            levels[depth].append(node)
            self._fillLevels(node.left, depth + 1, levels)
            self._fillLevels(node.right, depth + 1, levels)
        else:
            if depth < len(levels):
                levels[depth].append(None)
            if depth + 1 < len(levels):
                self._fillLevels(None, depth + 1, levels)
                self._fillLevels(None, depth + 1, levels)

    def drawTree(self):
        turtle.clear()
        turtle.speed(100)
        turtle.hideturtle()
        self._drawTree(self.root)
        while True:
            if keyboard.is_pressed('Enter'):
                break

    def _drawTree(self,node, x=0, y=200, dx=100, dy=50, radius=20):
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




