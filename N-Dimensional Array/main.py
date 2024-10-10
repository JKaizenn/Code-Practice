# You are given an N-dimensional array (a nested list) and your task is to convert it into a 1D array. The N-dimensional array can have any number of nested lists and each nested list can contain any number of elements. The elements in the nested lists are integers. Write a function that takes an N-dimensional array as input and returns a 1D array.

# Example 1:

# Input:

# array = [1, [2, 3], [4, [5, 6]], 7]
# Output:

# flatten_array(array) -> [1, 2, 3, 4, 5, 6, 7]
# Example 2:

# Input:

# array = [[1, 2], [3, 4], [5, 6]]
# Output:

# flatten_array(array) -> [1, 2, 3, 4, 5, 6]


nested_list = [1, [2, 3], [4, [5, 6]], 7]

def flatten_array(nested_list):
    flat_list = []
    for i in nested_list:
        if type(i) == list:
            flat_list.extend(flatten_array(i))
        else:
            flat_list.append(i)
    return flat_list

print(flatten_array(nested_list))