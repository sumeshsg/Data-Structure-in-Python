def island_count(grid):
    visited = set()
    count = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if explore(grid, i, j, visited):
                count += 1
    return count


def explore(grid, i, j, visited):
    if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
        return False
    if grid[i][j] == 'w':
        return False
    if (i, j) in visited:
        return False
    visited.add((i, j))
    explore(grid, i - 1, j, visited)
    explore(grid, i + 1, j, visited)
    explore(grid, i, j - 1, visited)
    explore(grid, i, j + 1, visited)
    return True


grid = [["w", "l", "w", "w", "w"],
        ["w", "l", "w", "w", "w"],
        ["w", "w", "w", "l", "w"],
        ["w", "w", "l", "l", "w"],
        ["l", "w", "w", "l", "l"],
        ["l", "l", "w", "w", "w"]]
print(island_count(grid))
