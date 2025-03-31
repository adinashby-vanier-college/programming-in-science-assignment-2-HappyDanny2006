# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.

def max_two_in_list(numbers):
    number1 = max(numbers)
    while number1 in numbers:
        numbers.remove(number1)
    if numbers == []:
        number2 = None
    else:
        number2 = max(numbers)
    return (number1, number2)

# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    
    unique_numbers.sort()
    return(unique_numbers)
# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    newlist = []  
    current_sum = 0  

    for num in arr:
        current_sum += num  
        newlist.append(current_sum)  

    return newlist

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    transposed = []  # List to hold the transposed matrix
    rows = len(matrix)  # Number of rows in the original matrix
    cols = len(matrix[0]) if rows > 0 else 0  # Number of columns in the original matrix

    for col in range(cols):  # Loop over columns
        new_row = []  # Create a new row for the transposed matrix
        for row in range(rows):  # Loop over rows
            new_row.append(matrix[row][col])  # Append the element from the original matrix
        transposed.append(new_row)  # Add the new row to the transposed matrix

    return transposed
# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    nth_elements = []
    for i in range(0, len(lst), step):
        nth_elements.append(lst[i])
    return nth_elements


# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    result = 0
    for i in range(len(list1)):
        result += list1[i] * list2[i]
    return(result)

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


