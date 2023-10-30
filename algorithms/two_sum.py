def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for index, num in enumerate(nums):
        res = target - num
        if res in nums and nums.index(res) != index:
            index2 = nums.index(res)
            return [index, index2]


nums = [2, 7, 11, 15]

if __name__ == "__main__":
    result = twoSum(nums, 9)
    print(result)
