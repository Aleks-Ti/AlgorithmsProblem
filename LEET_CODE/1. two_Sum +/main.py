def twoSum(nums, target):
    for i in range(len(nums)):
        for k in range(i + 1, len(nums)):
            if nums[i] + nums[k] == target:
                return i, k


if __name__ == '__main__':
    array = [int(x) for x in str(input()).split()]
    target = int(input())
    print(twoSum(array, target))
    # print(twoSum([2, 7, 11, 15], 9))
