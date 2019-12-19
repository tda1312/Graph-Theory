import pandas as pd
import numpy as np

def calculate_degree(input):
    degree = np.zeros(len(input))

    sum_col = input.sum(axis=0)
    sum_row = input.sum(axis=1)

    degree = (sum_col + sum_row)

    A = input.diagonal()
    d = A.flat
    diagMat = list(d)

    print("\nCalculate degree for non-directed graph:\n\n", np.diag(degree - diagMat))

    print("\nCalculate degree for directed graph:\n\n", np.diag(sum_col - diagMat))

def check_path(a, b, graph, vertices):
    visited = [False]*(vertices)

    queue = []

    queue.append(a)
    visited[a] = True

    while queue:
        n = queue.pop(0)

        if n == b:
            return True
        
        for i in graph(n):
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

    return False

input_matrix = np.loadtxt('./example.txt', dtype=int, usecols=range(10))
print("Input matrix:\n\n", input_matrix)

calculate_degree(input_matrix)

x = int(input("Enter starting point: "))
y = int(input("Enter ending point: "))

if check_path(x, y, input, 10):
    print("\nThere is a path from %d to %d" % (x, y))
else:
    print("\nThere is no path from %d to %d" % (x, y))