import functools


def get_maximum_array(*num_arrays: list[int]) -> list[int]:
    len_of_arrays = list(map(
        lambda num_array: len(num_array),
        num_arrays
    ))
    max_size = functools.reduce(max, len_of_arrays)

    for num_array in num_arrays:
        deficit = max_size - len(num_array)
        num_array.extend([0] * deficit)

    return list(map(max, *num_arrays))


def get_maximum_array_from_array(num_list: list[list[int]]) -> list[int]:

    return get_maximum_array(*num_list)


print(get_maximum_array_from_array([[1, 3, 7], [5, 1]]))