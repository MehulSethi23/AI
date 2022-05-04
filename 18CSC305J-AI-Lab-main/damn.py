#
# from queue import PriorityQueue
#
# n = int(input())
# graph=[]
# for i in range(n):
#     graph.append([])
#
# def best_first_search(source, target, n):
#     visited = [False] * n
#     visited[source] = True
#     pq = PriorityQueue()
#     pq.put((0, source))
#     while pq.empty() == False:
#         u = pq.get()[1]
#         # Displaying the path having lowest cost
#         print(u, end=" ")
#         if u == target:
#             break
#
#         for v, c in graph[u]:
#             if visited[v] == False:
#                 visited[v] = True
#                 pq.put((c, v))
#     print()
#
#
#
#
# for i in range(0,n-1):
#     x,y,cost=map(int,input().split())
#     graph[x].append((y, cost))
#     graph[y].append((x, cost))
#
# source= int(input())
# target = int(input())
#
# best_first_search(source, target,n)


# 14
# 0 1 3
# 0 2 6
# 0 3 5
# 1 4 9
# 1 5 8
# 2 6 12
# 2 7 14
# 3 8 7
# 8 9 5
# 8 10 6
# 9 11 1
# 9 12 10
# 9 13 2
# 0
# 9
# 0 1 3 2 8 9


import math


import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Markdown
from glob2 import glob

PATH = '/content/enishtein.png'


def G(x, mean, std):
    return np.exp(-0.5 * np.square((x - mean) / std))


def ExtremelyDark(x, M):
    return G(x, -50, M / 6)


def VeryDark(x, M):
    return G(x, 0, M / 6)


def Dark(x, M):
    return G(x, M / 2, M / 6)


def SlightlyDark(x, M):
    return G(x, 5 * M / 6, M / 6)


def SlightlyBright(x, M):
    return G(x, M + (255 - M) / 6, (255 - M) / 6)


def Bright(x, M):
    return G(x, M + (255 - M) / 2, (255 - M) / 6)


def VeryBright(x, M):
    return G(x, 255, (255 - M) / 6)


def ExtremelyBright(x, M):
    return G(x, 305, (255 - M) / 6)


for M in (128, 64, 192):
    x = np.arange(-50, 306)

    ED = ExtremelyDark(x, M)
    VD = VeryDark(x, M)
    Da = Dark(x, M)
    SD = SlightlyDark(x, M)
    SB = SlightlyBright(x, M)
    Br = Bright(x, M)
    VB = VeryBright(x, M)
    EB = ExtremelyBright(x, M)

    plt.figure(figsize=(20, 5))
    plt.plot(x, ED, 'k-.', label='ED', linewidth=1)
    plt.plot(x, VD, 'k-', label='VD', linewidth=2)
    plt.plot(x, Da, 'g-', label='Da', linewidth=2)
    plt.plot(x, SD, 'b-', label='SD', linewidth=2)
    plt.plot(x, SB, 'r-', label='SB', linewidth=2)
    plt.plot(x, Br, 'c-', label='Br', linewidth=2)
    plt.plot(x, VB, 'y-', label='VB', linewidth=2)
    plt.plot(x, EB, 'y-.', label='EB', linewidth=1)
    plt.plot((M, M), (0, 1), 'm--', label='M', linewidth=2)
    plt.plot((0, 0), (0, 1), 'k--', label='MinIntensity', linewidth=2)
    plt.plot((255, 255), (0, 1), 'k--', label='MaxIntensity', linewidth=2)
    plt.legend()
    plt.xlim(-50, 305)
    plt.ylim(0.0, 1.01)
    plt.xlabel('Pixel intensity')
    plt.ylabel('Degree of membership')
    plt.title(f'M={M}')
    plt.show()


def OutputFuzzySet(x, f, M, thres):
    x = np.array(x)
    result = f(x, M)
    result[result > thres] = thres
    return result


def AggregateFuzzySets(fuzzy_sets):
    return np.max(np.stack(fuzzy_sets), axis=0)


def Infer(i, M, get_fuzzy_set=False):
    VD = VeryDark(i, M)
    Da = Dark(i, M)
    SD = SlightlyDark(i, M)
    SB = SlightlyBright(i, M)
    Br = Bright(i, M)
    VB = VeryBright(i, M)

    x = np.arange(-50, 306)
    Inferences = (
        OutputFuzzySet(x, ExtremelyDark, M, VD),
        OutputFuzzySet(x, VeryDark, M, Da),
        OutputFuzzySet(x, Dark, M, SD),
        OutputFuzzySet(x, Bright, M, SB),
        OutputFuzzySet(x, VeryBright, M, Br),
        OutputFuzzySet(x, ExtremelyBright, M, VB)
    )

    fuzzy_output = AggregateFuzzySets(Inferences)
    if get_fuzzy_set:
        return np.average(x, weights=fuzzy_output), fuzzy_output
    return np.average(x, weights=fuzzy_output)


