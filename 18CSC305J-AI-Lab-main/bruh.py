

def dfs(root,g,vis,c):

    vis[root]=1
    for i in range(0,len(g[root])):
        if vis[g[root][i]] == 0:
            vis[g[root][i]] = 1

            dfs(g[root][i],g,vis,c+1)
            # print(root,c,vis)
        else:
            continue
    return


def bfs(root,g,vis,c):
    q=[]
    q.append(root)
    vis[root] = 1
    while(len(q)!=0):
        val=q[0]
        print(val)
        q=q[1:]
        for i in range(0,len(g[val])):
            if vis[g[val][i]] == 0:
                q.append(g[val][i])
                vis[g[val][i]] = 1
    return

n=int(input())
g=[]
for i in range(n):
    g.append([])
for i in range(n-1):
    u,v=map(int,input().split())
    g[u].append(v)
    g[v].append(u)
print(g)

vis=[]
for i in range(n):
    vis.append(0)

dfs(0,g,vis,0)

vis=[]
for i in range(n):
    vis.append(0)
bfs(0,g,vis,0)


#7
# 0 1
# 0 2
# 0 3
# 1 4
# 2 5
# 5 6
