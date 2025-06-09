def update_dictionary(dct, key, value):

    #Check if dct is a dictionary
    if not isinstance (dct, dict):
        return "Error: First argument must be a dictionary"

    #if the key already exists, print the original value
    if key in dct:
        print(f"Original value for '{key}': {dct[key]}")

    #Update or add the key-value pair
    dct[key] = value
    return dct
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    return


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26
