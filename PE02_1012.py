import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]

    for i in range(4):
        nx= x + dx[i]
        ny= y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n) and graph[ny][nx] == 1:
        # if (graph[ny][nx] == 1) and (0 <= nx < m) and (0 <=ny < n):
            graph[ny][nx] = -1
            dfs(nx, ny)


T = int(input())
for _ in range(T):
    m, n, N= map(int, input().split())
    graph= [[0]*(m) for _ in range(n)]

    for _ in range(N):
        x, y = map(int, input().split())
        graph[y][x] = 1 # x랑 y를 왜 바꿔야하지..

    cnt= 0
    for a in range(m):
        for b in range(n):
            if graph[b][a] == 1:
                dfs(a,b)
                cnt += 1
    print(cnt)


# # 1. BFS로 인접한 1을 0으로 바꿔줌.
# # 2. 행렬을 만들어 matrix[x][y] = 1인 경우 BFS로 실행. 한 번 실행될 때마다 cnt += 1
# # 3. BFS 함수가 인접한 모든 1을 0으로 바꾸므로 연결된 하나의 블럭 개수를 구할 수 있음

# T = int(input()) #테스트케이스의 개수

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def BFS(x,y):           
#     queue = [(x,y)]
#     matrix[x][y] = 0 # 방문처리

#     while queue:
#         x,y = queue.pop(0)

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or nx >= M or ny < 0 or ny >= N:
#                 continue

#             if matrix[nx][ny] == 1 :
#                 queue.append((nx,ny))
#                 matrix[nx][ny] = 0

# # 행렬만들기
# for i in range(T):
#     M, N, K = map(int,input().split())
#     matrix = [[0]*(N) for _ in range(M)]
#     cnt = 0

#     for j in range(K):
#         x,y = map(int, input().split())
#         matrix[x][y] = 1

#     for a in range(M):
#         for b in range(N):
#             if matrix[a][b] == 1:
#                 BFS(a,b)
#                 cnt += 1

#     print(cnt)

