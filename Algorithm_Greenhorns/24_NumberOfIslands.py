grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

def numIslands(grid):

    count = 0
    queue = []
    visited = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            #visited.append([i, j])
            #print (grid[i][j])
            if grid[i][j] == '1' and grid[i][j] not in visited: # 이것 뿐만 아니라 상하좌우도 체크
                count += 1
                print('yes')



# 하나씩 방문하면서 값이 1인지 체크
# 값이 1이고 visited에 속하지 않으면서 visited의 상하좌우에 속하지 않으면 count + 1


numIslands(grid)

