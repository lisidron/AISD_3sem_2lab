from BSTree import BSTree

tree = BSTree()

tree.insert(10)
tree.drawTree()
[tree.insert(x) for x in range(9)]
tree.drawTree()

tree.delete(10)
tree.drawTree()

print(tree.search(10))
print(tree.search(9))

print(tree.search(11))

print(tree.getHeight())

print(0)
print(tree.inorder(tree.root))
print(tree.preorder(tree.root))
print(tree.postorder(tree.root))
print(tree.levelOrder())
