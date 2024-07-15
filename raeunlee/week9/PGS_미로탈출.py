from collections import deque

def bfs(start, end, maps):
	# 탐색할 방향
    dy = [0, 1, -1, 0]
    dx = [1, 0, 0, -1]
    
    n = len(maps)       # 세로
    m = len(maps[0])    # 가로
    
    visited = [[False] * m for _ in range(n)]
    que = deque()
    flag = False
    
    for i in range(n):
        for j in range(m):
        	# 시작점 찾으면 시작점과 카운트 0 기록
            if maps[i][j] == start:      
                que.append((i, j, 0))    
                visited[i][j] = True
                flag = True; break 
        if flag: break
                
    # BFS 
    while que:
        y, x, cost = que.popleft()
        
        # end 찾으면 return
        if maps[y][x] == end:
            return cost
        # 아직 안찾았으면 탐색한다
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            # maps 범위내에서 벽이 아닌경우
            if 0<= ny <n and 0<= nx <m and maps[ny][nx] !='X':
                if not visited[ny][nx]:
                    que.append((ny, nx, cost+1))
                    visited[ny][nx] = True
                    
    return -1	# 탈출할 수 없다면
        
            
def solution(maps):
    path1 = bfs('S', 'L', maps)	# s -> l 
    path2 = bfs('L', 'E', maps) # l -> e
    
    # 둘다 -1 이 아니라면 탈출할 수 있음
    if path1 != -1 and path2 != -1:
        return path1 + path2
        
   	# 둘중 하나라도 -1 이면 탈출불가
    return -1
