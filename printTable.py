tableData=[['apples','oranges','cherries','bananas'],
           ['Alice','Bob','Carol','David'],
           ['dogs','cats','moose','goose']]

def printTable(table):
    colWidth=[0]*len(table)
    lin=len(table)
    col=len(table[0])
    print(lin)
    print(col)
    print(colWidth)
    # find the width of each column of text
    for i in range(lin):
        for j in range(col):
            if colWidth[i] < len(table[i][j]):
                colWidth[i] = len(table[i][j])
    print(colWidth)
    # print the table
    for j in range(col):
        for i in range(lin):
            print(table[i][j].rjust(colWidth[i]),end=' ')
        print('')

printTable(tableData)