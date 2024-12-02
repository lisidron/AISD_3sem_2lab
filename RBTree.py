import random
import turtle
import keyboard

class Node:
    def __init__(self, key, color):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = color  # True - red, False - black

class RBTree:
    def __init__(self):
        self.TNULL = Node(0, False)
        self.root = self.TNULL
        self.TNULL.right = self.TNULL
        self.TNULL.parent = None
        self.root = self.TNULL


    def insertBestCase(self, key):
        key = sorted(key)
        for key in key:
            self.insert(key)


    def insertWorstCase(self, key):
        for key in key:
            self.insert(key)


    def insertAvCase(self, key):
        random.shuffle(key)
        for key in key:
            self.insert(key)


    def search(self, key):
        node = self._search(key)
        return node != self.TNULL

    def _search(self, key, node=None):
        if node is None:
            node = self.root

        while node != self.TNULL and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right

        return node

    def insert(self, key):
        new_node = Node(key, True)
        new_node.left = new_node.right = self.TNULL

        parent = None
        current = self.root

        while current != self.TNULL:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = True
        self.insertFix(new_node)

    def insertFix(self, node):
        while node.parent and node.parent.color:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle and uncle.color:
                    node.parent.color = False
                    uncle.color = False
                    node.parent.parent.color = True
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = False
                    node.parent.parent.color = True
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle and uncle.color:
                    node.parent.color = False
                    uncle.color = False
                    node.parent.parent.color = True
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = False
                    node.parent.parent.color = True
                    self.left_rotate(node.parent.parent)

        self.root.color = False

    def delete(self, key):
        node = self._search(key)
        if node == self.TNULL:
            return

        y = node
        y_original_color = y.color
        if node.left == self.TNULL:
            x = node.right
            self.transplant(node, node.right)
        elif node.right == self.TNULL:
            x = node.left
            self.transplant(node, node.left)
        else:
            y = self.minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y

            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color

        if y_original_color == False:
            self.deleteFix(x)

    def deleteFix(self, x):
        while x != self.root and not x.color:
            if x == x.parent.left:
                sibling = x.parent.right
                if sibling.color:
                    sibling.color = False
                    x.parent.color = True
                    self.left_rotate(x.parent)
                    sibling = x.parent.right

                if not sibling.left.color and not sibling.right.color:
                    sibling.color = True
                    x = x.parent
                else:
                    if not sibling.right.color:
                        sibling.left.color = False
                        sibling.color = True
                        self.right_rotate(sibling)
                        sibling = x.parent.right

                    sibling.color = x.parent.color
                    x.parent.color = False
                    sibling.right.color = False
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                sibling = x.parent.left
                if sibling.color:
                    sibling.color = False
                    x.parent.color = True
                    self.right_rotate(x.parent)
                    sibling = x.parent.left

                if not sibling.left.color and not sibling.right.color:
                    sibling.color = True
                    x = x.parent
                else:
                    if not sibling.left.color:
                        sibling.right.color = False
                        sibling.color = True
                        self.left_rotate(sibling)
                        sibling = x.parent.left

                    sibling.color = x.parent.color
                    x.parent.color = False
                    sibling.left.color = False
                    self.right_rotate(x.parent)
                    x = self.root

        x.color = False

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def inorder(self):
        def _inorder(node):
            if node != self.TNULL:
                yield from _inorder(node.left)
                yield str(node.key)
                yield from _inorder(node.right)

        return " ".join(_inorder(self.root))

    def preorder(self):
        def _preorder(node):
            if node != self.TNULL:
                yield str(node.key)
                yield from _preorder(node.left)
                yield from _preorder(node.right)

        return " ".join(_preorder(self.root))

    def postorder(self):
        def _postorder(node):
            if node != self.TNULL:
                yield from _postorder(node.left)
                yield from _postorder(node.right)
                yield str(node.key)

        return " ".join(_postorder(self.root))


    def levelOrder(self):
        return " ".join(self._levelOrder())

    def _levelOrder(self):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node != self.TNULL:
                yield "".join(str(node.key))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)




    def getHeight(self, node=None):
        if node is None:
            node = self.root

        if node == self.TNULL:
            return 0

        left_height = self.getHeight(node.left)
        right_height = self.getHeight(node.right)
        return max(left_height, right_height) + 1

    def drawTree(self):
        turtle.clear()
        turtle.speed(100)
        turtle.hideturtle()
        self._drawTree(self.root)

        while True:
            if keyboard.is_pressed('Enter'):
                turtle.penup()
                break




    def _drawTree(self,node, x=0, y=200, dx=150, dy=50, radius=20):
        if node is None:
            return

        self.drawNode(x, y, radius, node.key, node.color)
        if node.left != self.TNULL:
            child_x = x - dx
            child_y = y - dy
            turtle.penup()
            turtle.goto(x, y - radius)
            turtle.pendown()
            turtle.goto(child_x, child_y + radius)
            self._drawTree(node.left, child_x, child_y, dx / 2, dy, radius)

        if node.right != self.TNULL:
            child_x = x + dx
            child_y = y - dy
            turtle.penup()
            turtle.goto(x, y - radius)
            turtle.pendown()
            turtle.goto(child_x, child_y + radius)
            self._drawTree(node.right, child_x, child_y, dx / 2, dy, radius)

    def drawNode(self, x, y, radius, label, color):
        turtle.penup()
        turtle.goto(x, y - radius)
        turtle.pendown()
        turtle.pencolor("red" if color else "black")
        turtle.circle(radius)
        turtle.penup()
        turtle.goto(x, y - radius)
        turtle.write(label, align="center", font=("Arial", 12, "normal"))
        turtle.pencolor("black")




