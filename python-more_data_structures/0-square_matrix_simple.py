def square_matrix_simple(matrix=[]):
    if not matrix:
        return []
    new_list = []
    for row in matrix:
        for value in row:
            new_list.append(value ** 2)
        
    return new_list        
    
    
