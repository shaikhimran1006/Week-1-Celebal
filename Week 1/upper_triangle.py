def upper_triangle(rows):
    print("\nUpper Triangular Pattern:\n")
    for i in range(rows, 0, -1):
        spaces = "  " * (rows - i)
        stars = "* " * i
        print(spaces + stars)

rows=int(input("enter the number of rows: "))
upper_triangle(rows)
