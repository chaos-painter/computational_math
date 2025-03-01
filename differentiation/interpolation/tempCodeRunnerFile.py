print("Forward Differences Table")
    
    num_rows = len(x)  
    num_cols = len(diffs) + 1
    
    table = [["" for _ in range(num_cols)] for _ in range(num_rows)]

    for i in range(num_rows):
        table[i][0] = str(x[i])

    for col in range(1, num_cols):
        for row in range(num_rows - col):
            table[row][col] = str(round(diffs[col - 1][row], 3))

    for row in table:
        print("\t".join(row))