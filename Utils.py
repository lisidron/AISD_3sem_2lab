from sys import setrecursionlimit
import pickle
import BSTree
import RBTree
import AVLTree


steps = [1, 10, 100, 1000, 5000, 10000, 15000, 20000, 30000, 50000, 70000, 80000, 100000]
setrecursionlimit(1000000000)
#Бинарное дерево поиска
bstDataWorst = []
bstDataAv = []
bstDataBest = []

#АВЛ дерево
avlData = []

#Красно-черное дерево
rbtDataWorst = []
rbtDataAv = []
rbtDataBest = []

for i in steps:
    keys = [j for j in range(i)]


    bsTreeWorst = BSTree.BSTree()
    bsTreeAv = BSTree.BSTree()
    bsTreeBest = BSTree.BSTree()

    avlTree = AVLTree.AVLTree()

    rbTreeWorst = RBTree.RBTree()
    rbTreeAv = RBTree.RBTree()
    rbTreeBest = RBTree.RBTree()

    #Вставка элементов
    bsTreeWorst.insert_worst_case(keys)
    bsTreeAv.insert_random_case(keys)
    bsTreeBest.insert_best_case(keys)

    for k in keys:
        avlTree.insert(k)
    print(i)
    rbTreeWorst.insert_worst_case(keys)
    rbTreeAv.insert_random_case(keys)
    rbTreeBest.insert_best_case(keys)


    bstDataWorst.append([i, bsTreeWorst.getHeight()])
    bstDataAv.append([i, bsTreeAv.getHeight()])
    bstDataBest.append([i, bsTreeBest.getHeight()])

    avlData.append([i, avlTree.getHeight()])

    rbtDataWorst.append([i, rbTreeWorst.getHeight()])
    rbtDataAv.append([i, rbTreeAv.getHeight()])
    rbtDataBest.append([i, rbTreeBest.getHeight()])





data = [
        bstDataWorst,
        bstDataAv,
        bstDataBest,
        avlData,
        rbtDataWorst,
        rbtDataAv,
        rbtDataBest]


with open("data.txt", 'w+', encoding="UTF-8") as file:
    for array in data:
        for sub_array in array:
            line = ' '.join(map(str, sub_array))
            file.write(line + '\n')
        file.write('-' * 20 + '\n')





