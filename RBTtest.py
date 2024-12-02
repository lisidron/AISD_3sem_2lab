from RBTree import RBTree

tree = RBTree()

tree.insert(10)
tree.drawTree()

tree.insertBestCase([x for x in range(10)])
tree.drawTree()

tree.insertWorstCase([x for x in range(10)])
tree.drawTree()

tree.delete(10)
tree.drawTree()
tree.insert(111)
print(tree.search(10))
print(tree.search(9))
print(tree.search(11))
print(tree.inorder())
print(tree.preorder())
print(tree.postorder())
print(tree.levelOrder())



