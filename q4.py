def string_reverse(s):
    # Check if the input is a string
    if isinstance(s, str):
        print("Yes, it is a string!")
    else:
        print("No, it is not a string.")
        return -1

    # Reverse the string using slicing
    reversed_string = s[::-1]

    return reversed_string


print(string_reverse("Hello World!"))
print(string_reverse("Phython"))
