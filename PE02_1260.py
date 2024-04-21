#vertex 개수, edge 개수, start vertex
#여러개 edge 가능, undirected

N, M, V= map(int, input().split())
graph= [[0]*(N+1) for _ in range(N+1)]

for i in range(M):              #vertex 수만큼 반복
    a, b= map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited1= [0]*(N+1)
visited2= visited1.copy()

def dfs(V):
    visited1[V]=1
    print(V, end=' ')
    for i in range(1, N+1):
        if (graph[V][i] and visited1[i] == 0):
            dfs(i)

def bfs(V):
    queue=[V]
    visited2[V]=1
    while queue:                #que가 비어있을때까지
        V= queue.pop(0)
        print(V, end= ' ')
        for i in range(1, N+1):
            if (graph[V][i] and visited2[i] == 0):
                queue.append(i)
                visited2[i]=1


dfs(V)
print()
bfs(V)