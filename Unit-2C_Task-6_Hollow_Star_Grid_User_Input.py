rows = 5
for row_loop_var in range(1, rows + 1):
    for col_loop_var in range(1, rows + 1):
        if (
            row_loop_var == 1
            or row_loop_var == rows
            or col_loop_var == 1
            or col_loop_var == rows
        ):
            print("*", end=" ")
        else:
             print(" ", end=" ")
    print()