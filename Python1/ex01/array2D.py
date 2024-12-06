

def slice_me(family: list, start: int, end: int) -> list:
"""
Slices a list based on start and end
"""
    if family.__class__ != list:
        raise ValueError("The input should be a list.")

    row_length = len(family[0]) if family else 0
    for row in family:
        if len(row) != row_length:
            raise ValueError("All rows must be of the same length.")

    shape = (len(family), len(family[0]))
    print(f"My shape is : {shape}")

    try:
        sliced_array = family[start:end]
    except IndexError:
        raise ValueError("Invalid start or end index.")

    if sliced_array:
        new_shape = (len(sliced_array), len(sliced_array[0]))
    else:
        new_shape = (0, 0)

    print(f"My new shape is : {new_shape}")

    return sliced_array
