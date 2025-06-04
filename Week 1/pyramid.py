def pyramid(rows):
    print("\nPyramid Pattern:\n")
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        stars = "* " * i
        print(spaces + stars)

rows=int(input("enter the no of rows: "))
pyramid(rows)