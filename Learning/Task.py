# rows = 5

# for i in range(rows):
#     for j in range(rows * 2 - 1):
#         if j == 0 or j == rows * 2 - 2:
#             print("*", end="")
#         elif i == j and j <= rows - 1:
#             print("*", end="")
#         elif i + j == rows * 2 - 2 and j >= rows - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

n = int(input("Enter the dimension: "))

width = 2 * n - 1

for row in range(n):
    for col in range(width):
        if (
            col == 0 or                
            col == width - 1 or               
            (row == col and col < n) or        
            (row + col == width - 1 and col >= n - 1)
        ):
            print("*", end="")
        else:
            print(" ", end="")
    print()
