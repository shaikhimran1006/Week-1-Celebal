def lower_triangle(rows):
    print("Lower Triangular Pattern:\n")
    for i in range(1, rows + 1):
        print("* " * i)

rows=int(input("enter the no of rows: "))
lower_triangle(rows)