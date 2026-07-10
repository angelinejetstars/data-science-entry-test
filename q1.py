def swap(x, y):
    # Return -1 if x and y is not numeric
    if not (isinstance(x, (int, float, complex))) and not (isinstance(y, (int, float, complex))):
        return -1

    # swap values inline without a third variable
    # tuple unpacking
    x, y = y, x

    # print the swapped values if both x and y are numeric
    print(f" x = {x}, y = {y}")

    return


swap("Apple", 10)
swap(9, 17)
