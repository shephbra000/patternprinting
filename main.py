def print_triangle_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print('*', end=' ')
        print()
number_of_rows = 5
print_triangle_pattern(number_of_rows)