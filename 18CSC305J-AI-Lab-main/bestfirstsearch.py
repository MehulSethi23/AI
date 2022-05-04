
from queue import PriorityQueue

n = int(input())
graph=[]
for i in range(n):
    graph.append([])

def best_first_search(source, target, n):
    visited = [False] * n
    visited[source] = True
    pq = PriorityQueue()
    pq.put((0, source))
    while pq.empty() == False:
        u = pq.get()[1]
        # Displaying the path having lowest cost
        print(u, end=" ")
        if u == target:
            break

        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))
    print()




for i in range(0,n-1):
    x,y,cost=map(int,input().split())
    graph[x].append((y, cost))
    graph[y].append((x, cost))

source= int(input())
target = int(input())

best_first_search(source, target,n)


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





