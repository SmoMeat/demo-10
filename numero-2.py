import functools

def maximum1(nums: list[int]) -> int:
    maximum_value: int = nums[0]
    for num in nums[1:]:
        if num > maximum_value:
            maximum_value = num
    return maximum_value

def maximum2(nums: list[int]) -> int:
    return functools.reduce(max, nums)

if __name__ == '__main__':
    print(maximum1([-3, 7, 3, 1, 9]))
    print(maximum2([-3, 7, 3, 1, 9]))
