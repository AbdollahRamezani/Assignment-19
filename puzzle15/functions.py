import random

def get_non_repeating_random_2d_list(n, m): 
  
    # Create an empty list 
    matrix = [] 
  
    # Create a list containing n*m numbers from 1 to n*m 
    # and shuffle it to get random permutation of numbers 
    nums = list(range(1, n * m + 1)) 
    random.shuffle(nums) 

    # Fill the empty list with shuffled numbers 
    for i in range(n): 

        # Create an empty sublist  
        row = []  

        for j in range(m):  

            # Get the last number from nums list and append it to row sublist.  
            row.append(nums.pop())  

        # Append the row sublist to matrix list.  
        matrix.append(row)  

    return matrix