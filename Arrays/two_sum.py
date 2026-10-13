def solve_two_sum(nums: list[int], target: int) -> list[int]:
    """returns a list of two indices of the numbers in nums that add up to target in O(n)"""
    prevMap = {}  # val: index

    for i, num in enumerate(nums):
        diff = target - num
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[num] = i

    return []
