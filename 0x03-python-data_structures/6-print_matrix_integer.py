def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for row in matrix:
        for index, col in enumerate(row):
            if index != len(row) - 1:
                print("{:d}".format(col), end=" ")
            else:
                print("{:d}".format(col))
