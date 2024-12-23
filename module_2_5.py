def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        inner_matrix = []
        for j in range(m):
            inner_matrix.append(value)
        matrix.append(inner_matrix)
    print(matrix)

get_matrix(2,2,10)
get_matrix(3,5,42)
get_matrix(4,2,13)
