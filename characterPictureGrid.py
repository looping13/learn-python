def drawPictureGrid(pGrid, transpose):
    if transpose:
        y = len(pGrid)
        x = len(pGrid[0])
    else:
        x = len(pGrid)
        y = len(pGrid[0])
    for i in range(x):
        for j in range(y):
            if transpose:
                print(pGrid[j][i], end='')
            else:
                print(pGrid[i][j], end='')

        print('')


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print('Heart')
x = len(grid)
y = len(grid[0])

print('original')
drawPictureGrid(grid,False)
print('Transpose')
drawPictureGrid(grid,True)
