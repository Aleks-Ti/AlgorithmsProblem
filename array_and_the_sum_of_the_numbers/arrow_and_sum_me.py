# массив с числами
nums = [2, 4, 5, 1, 8]

# сумма
target = 155


def twoSum(nums, target):
    for i in range(len(nums)):
        asd = [j for j in range(i + 1) if target == nums[i] + nums[j]]