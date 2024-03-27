import functools

def get_maximum_array(nums1: list[int], nums2: list[int]) -> list[int]:
    if len(nums1) >= len(nums2):
        longer_array = nums1 
        shortest_array = nums2
    else:
        longer_array = nums2
        shortest_array = nums1

    to_return = list(map(max, longer_array, shortest_array))
    to_return.extend(longer_array[len(shortest_array):])
    
    return to_return

print(get_maximum_array([0, 3], [3,2,3]))