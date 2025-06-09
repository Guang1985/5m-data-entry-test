def find_and_replace(lst, find_val, replace_val):
#check if lst is a list
    if not isinstance (lst, list):
        return "Error: First argument must be a list"


    #replace all occurances of find_val with replace_val
    for i in range (len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val

    return lst
    
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    return


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print("Result 1:", result 1)

result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print("Result2:", result2)
