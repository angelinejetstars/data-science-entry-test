def find_and_replace(lst, find_val, replace_val):

    # lst must be a list
    if isinstance(lst, list):
        print("Yes, it is a list!")
    else:
        print("No, it is not a list.")
        return -1

    # Create a function that searches for all occurrences of a value (find_val)
    # in a given list (lst)
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val

    # replace them with another value (replace_val)

    # return the modified list
    print(lst)
    return lst


find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)

find_and_replace(["apple", "banana", "apple"], "apple", "orange")
