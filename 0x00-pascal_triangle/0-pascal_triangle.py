#!/usr/bin/python3
"""
Module for Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Function that returns a list of lists of integers representing
    the Pascal's triangle of n.
    
    Args:
        n (int): Number of rows in Pascal's Triangle
        
    Returns:
        list: A list of lists containing integers representing Pascal's Triangle
              Returns an empty list if n <= 0
    """
    if n <= 0:
        return []
    
    triangle = [[1]]  # Initialize with the first row
    
    for i in range(1, n):
        # Previous row
        prev_row = triangle[-1]
        # Start new row with 1
        current_row = [1]
        
        # Calculate middle values for current row
        for j in range(1, i):
            # Each value is the sum of the two values above it
            current_row.append(prev_row[j-1] + prev_row[j])
        
        # End the row with 1
        current_row.append(1)
        
        # Add the current row to the triangle
        triangle.append(current_row)
    
    return triangle
