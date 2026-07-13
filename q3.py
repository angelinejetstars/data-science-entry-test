def update_dictionary(dct, key, value):

    # Check if the key already exists in the dct, print the original value
    if key in dct:
        print(f"Original value already exist for '{key}': {dct[key]}")

    # then update its value
    # return the updated dictionary
    dct[key] = value

    return dct


dict1 = {}
result1 = update_dictionary(dict1, "name", "Alice")
print("Result 1:", result1)  # Output: {'name': 'Alice'}

dict2 = {"age": 25, "name": "John"}
result2 = update_dictionary(dict2, "age", 26)
print("Result 2:", result2)  # Output: {'age': 26, 'name': 'John'}
  
  
