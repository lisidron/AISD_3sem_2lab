import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

import ideal_graph


data = []
with open("data.txt", 'r', encoding="UTF-8") as file:
    lines = file.readlines()
    i = 0
    while i < len(lines):
        array = []
        while i < len(lines) and '-' not in lines[i]:
            try:
                sub_array = list(map(int, lines[i].split()))
                array.append(sub_array)
            except ValueError:
                pass
            i += 1
        data.append(array)
        i += 1

steps = [1, 10, 100, 1000, 5000, 10000, 15000, 20000, 30000, 50000, 70000, 80000, 100000]
def theryData(func):
    dots = []
    limits = [i for i in range(min(steps), max(steps))]
    for i in limits:
        dots.append([i, func(i)])
    return dots


bstDataWorst, bstDataAv, bstDataBest, avlDataAll, rbtDataWorst, rbtDataAv, rbtDataBest = data

bstData = [["Бинарное дерево поиска", bstDataWorst], ["Бинарное дерево поиска", bstDataAv], ["Бинарное дерево поиска", bstDataBest]]
avlData = [["Эвл дерево", avlDataAll], ["Эвл дерево", avlDataAll], ["Эвл дерево", avlDataAll]]
rbtData = [["Черно-красное дерево", rbtDataWorst], ["Черно-красное дерево", rbtDataAv], ["Черно-красное дерево", rbtDataBest]]
dataPractical =[bstData, avlData, rbtData]

bstDataTheory = [["Бинарное дерево поиска", theryData(ideal_graph.bstWorst)], ["Бинарное дерево поиска", theryData(ideal_graph.bstAv)], ["Бинарное дерево поиска", theryData(ideal_graph.bstBest)]]
avlDataTheory = [["Эвл дерево", theryData(ideal_graph.avlWorst)], ["Эвл дерево", theryData(ideal_graph.avlAv)], ["Эвл дерево", theryData(ideal_graph.avlBest)]]
rbtDataTheory = [["Черно-красное дерево", theryData(ideal_graph.rbtWorst)], ["Черно-красное дерево", theryData(ideal_graph.rbtAv)], ["Черно-красное дерево", theryData(ideal_graph.rbtBest)]]
dataTheory = [bstDataTheory, avlDataTheory, rbtDataTheory]

titles = ["Худший случай", "Средний случай", "Лучший случай"]

def oncePlotTheory(data, title):
    points = data[1]
    points = np.array(points)
    x = points[:, 0]
    y = points[:, 1]


    plt.plot(x, y, color='purple', label="Теоретические данные",
                 zorder=10)


    plt.xlabel('Количество элементов, n')
    plt.ylabel('Высота, h')
    plt.title(data[0] + ". " + title)
    plt.legend()
    plt.grid(True)
    plt.savefig(f"теория/{data[0]} {title}.png")
    plt.close()

def multiPlotTheory(allData, titles):
    colors = ['purple', 'orange', 'brown', 'pink', 'gray', 'olive', 'cyan', 'blue', 'green', 'red']
    i=0
    for data in allData:
        points = data[1]
        points = np.array(points)
        x = points[:, 0]
        y = points[:, 1]

        plt.plot(x, y, color=colors[i], label=titles[i],
                 zorder=10)
        i+=1

    plt.xlabel('Количество элементов, n')
    plt.ylabel('Высота, h')
    plt.title("Все случаи высоты. " + allData[0][0])
    plt.legend()
    plt.grid(True)
    plt.savefig(f"теория/{allData[0][0]}.png")
    plt.close()

def oncePlotPointsPractic(data, title):
    points = data[1]
    x = np.array([point[0] for point in points])
    y = np.array([point[1] for point in points])

    plt.scatter(x, y, color='orange', label='Экспериментальные данные', zorder=5)

    plt.xlabel('Количество элементов, n')
    plt.ylabel('Высота, h')
    plt.title(f'{data[0]}. {title}')
    plt.legend()
    plt.grid(True)

    plt.savefig(f"практика/{data[0]} {title}.png")
    plt.close()


def oncePlotRegressionPractic(data, title):
    points = data[1]
    points = np.array(points)
    x = points[:, 0]
    y = points[:, 1]

    slope_linear, intercept_linear, r_value_linear, _, _ = stats.linregress(x, y)
    y_pred_linear = intercept_linear + slope_linear * x
    r_squared_linear = r_value_linear ** 2

    x_log2 = np.log2(x)
    slope_log, intercept_log, r_value_log, _, _ = stats.linregress(x_log2, y)
    y_pred_log = intercept_log + slope_log * np.log2(x)
    r_squared_log = r_value_log ** 2

    if r_squared_linear > r_squared_log:
        best_model = "Линейная регрессия"
        best_model_eq = f"y = {intercept_linear:.3f} + {slope_linear:.3f}x"
        best_y_pred = y_pred_linear
    else:
        best_model = "Логарифмическая регрессия"
        best_model_eq = f"y = {intercept_log:.3f} + {slope_log:.3f}*log2(x)"
        best_y_pred = y_pred_log


    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='orange', label='Данные', zorder=5)

    if best_model == "Линейная регрессия":
        plt.plot(x, best_y_pred, color='purple', label=f'Экспериментальные данные', zorder=10)
    else:
        x_dense = np.linspace(min(x), max(x), 1000)
        y_dense = intercept_log + slope_log * np.log2(x_dense)
        plt.plot(x_dense, y_dense, color='purple', label=f'Экспериментальные данные', zorder=10)

    plt.xlabel('Количество элементов, n')
    plt.ylabel('Высота, h')
    plt.title(f'Регрессия {data[0]}. {title}')
    plt.legend()
    plt.grid(True)
    plt.savefig(f"практика/Регрессия {data[0]} {title}.png")
    plt.close()

    print(f"Уравнение {data[0]} {title}: {best_model_eq}")

def multiPlotRegressionPractic(allData, titles):
    colors = ['purple', 'orange', 'brown', 'pink', 'gray', 'olive', 'cyan', 'blue', 'green', 'red']
    i = 0

    for data in allData:
        points = data[1]
        points = np.array(points)
        x = points[:, 0]
        y = points[:, 1]

        slope_linear, intercept_linear, r_value_linear, _, _ = stats.linregress(x, y)
        y_pred_linear = intercept_linear + slope_linear * x
        r_squared_linear = r_value_linear ** 2

        x_log2 = np.log2(x)
        slope_log, intercept_log, r_value_log, _, _ = stats.linregress(x_log2, y)
        y_pred_log = intercept_log + slope_log * np.log2(x)
        r_squared_log = r_value_log ** 2

        if r_squared_linear > r_squared_log:
            best_model = "Линейная регрессия"
            best_model_eq = f"y = {intercept_linear:.3f} + {slope_linear:.3f}x"
            best_y_pred = y_pred_linear
        else:
            best_model = "Логарифмическая регрессия"
            best_model_eq = f"y = {intercept_log:.3f} + {slope_log:.3f}*log2(x)"
            best_y_pred = y_pred_log

        if best_model == "Линейная регрессия":
            plt.plot(x, best_y_pred, color=colors[i], label=titles[i], zorder=10)
        else:
            x_dense = np.linspace(min(x), max(x), 1000)
            y_dense = intercept_log + slope_log * np.log2(x_dense)
            plt.plot(x_dense, y_dense, color=colors[i], label=titles[i], zorder=10)
        i+=1


    plt.xlabel('Количество элементов, n')
    plt.ylabel('Высота, h')
    plt.title(f'{allData[0][0]}. Сравнение различных случаев')
    plt.legend()
    plt.grid(True)
    plt.savefig(f"практика/Сводный Регрессия{allData[0][0]}.png")
    plt.close()

for i in dataTheory:
    oncePlotTheory(i[0], titles[0])
    oncePlotTheory(i[1], titles[1])
    oncePlotTheory(i[2], titles[2])
multiPlotTheory(bstDataTheory, titles)
multiPlotTheory(avlDataTheory, titles)
multiPlotTheory(rbtDataTheory, titles)

for i in dataPractical:
    oncePlotPointsPractic(i[0], titles[0])
    oncePlotPointsPractic(i[1], titles[1])
    oncePlotPointsPractic(i[2], titles[2])

for i in dataPractical:
    oncePlotRegressionPractic(i[0], titles[0])
    oncePlotRegressionPractic(i[1], titles[1])
    oncePlotRegressionPractic(i[2], titles[2])

multiPlotRegressionPractic(bstData, titles)
multiPlotRegressionPractic(avlData, titles)
multiPlotRegressionPractic(rbtData, titles)
