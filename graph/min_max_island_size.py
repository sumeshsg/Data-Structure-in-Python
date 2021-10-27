def min_or_max_island(grid, is_max=True):
    visited = set()
    count = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            result = explore(grid, i, j, visited)
            if result:
                count = result if count == 0 else count
                if is_max:
                    count = max(result, count)
                else:
                    count = min(result, count)

    return count


def explore(grid, i, j, visited):
    if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
        return False
    if grid[i][j] == 'w':
        return False
    if (i, j) in visited:
        return False
    cnt = 1
    visited.add((i, j))
    cnt += explore(grid, i - 1, j, visited)
    cnt += explore(grid, i + 1, j, visited)
    cnt += explore(grid, i, j - 1, visited)
    cnt += explore(grid, i, j + 1, visited)
    return cnt


grid = [["w", "l", "w", "l", "w"],
        ["w", "l", "w", "w", "w"],
        ["w", "w", "w", "l", "w"],
        ["w", "w", "l", "l", "w"],
        ["l", "l", "l", "l", "l"],
        ["l", "l", "w", "w", "w"]]
print(min_or_max_island(grid, True))
print(min_or_max_island(grid, False))
