import pandas as pd
import numpy as np

def calculate_degree(matrix):
    degree = np.zeros(len(matrix))

    sum_col = matrix.sum(axis=0)
    sum_row = matrix.sum(axis=1)

    degree = (sum_col + sum_row)

    A = matrix.diagonal()
    d = A.flat
    diagMat = list(d)

    print("\nCalculate number of degrees for directed graph:\n\n", np.diag(degree - diagMat))

    print("\nCalculate number of degrees for non-directed graph:\n\n", np.diag(sum_col - diagMat))

    return np.diag(sum_col - diagMat)

def check_DFS(matrix, j, visited):
    
    visited[j] = True

    for i in matrix[j]:
        if visited[i] == False:
            check_DFS(matrix, i, visited)

def check_connected(matrix, vertices):
    
    visited = [False]*(vertices)

    for i in range(vertices):
        if len(matrix[i]) > 1:
            break

    if i == (vertices - 1):
        return True

    check_DFS(matrix, i, visited)

    for i in range(vertices):
        if visited[i] == False and len(matrix[i]) > 0:
            return False

    return True

def check_euler_circuit(matrix, vertices):
    # if check_connected(matrix, vertices) == False:
    #     return 0
    # else:
        odd = 0
        for i in range(vertices):
            for j in range(vertices):
                if (matrix[i][j] != 0):
                    print("\nVertice: ", i)
                    print("Check number of degree: ", matrix[i][j])
                if ((matrix[i][j] % 2) != 0):
                    odd += 1
            print("-> Number of odd values: ", odd)
        
        if odd == 0:
            return 2
        elif odd == 2:
            return 1
        elif odd > 2:
            return 0

def check(matrix, vertices):
    print("\n\n---------checking---------")
    result = check_euler_circuit(matrix, vertices)
    if result == 0:
        print("you get nothing, good day sir!")
    elif result == 1:
        print("graph has an Euler path")
    else:
        print("graph has an Euler circuit")

# def check_path(a, b, graph, vertices):
#     visited = [False]*(vertices)

#     queue = []

#     queue.append(a)
#     visited[a] = True

#     while queue:
#         n = queue.pop(0)

#         if n == b:
#             return True
        
#         for i in graph(n):
#             if visited[i] == False:
#                 queue.append(i)
#                 visited[i] = True

#     return False
input_file = input("Enter file name: ")
input_matrix = np.loadtxt(input_file, dtype=int)
print("Input matrix:\n\n", input_matrix)

check_matrix = calculate_degree(input_matrix)
print("\nmatrix for checking: \n\n", check_matrix)

check(check_matrix, len(input_matrix))

# x = int(input("Enter starting point: "))
# y = int(input("Enter ending point: "))

# if check_path(x, y, input, 10):
#     print("\nThere is a path from %d to %d" % (x, y))
# else:
#     print("\nThere is no path from %d to %d" % (x, y))