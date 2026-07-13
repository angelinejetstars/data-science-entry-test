def find_first_negative(lst):

    # use while loop to find first negative number in a list (lst)
    index = 0
    i_len_list = len(lst)

    while index < i_len_list:
        if lst[index] < 0:

            # return the first negative number if found
            return lst[index]

    # move to next item in list
        index += 1

    # otherwise return "No negatives"
    return "No negatives"


list1 = [3, 5, -1, -2, 8]
result1 = find_first_negative(list1)
print("Result 1:", result1)  # Output: -1

list2 = [2, 10, 7, 0]
result2 = find_first_negative(list2)
print("Result 2:", result2)  # Output: "No negatives"
