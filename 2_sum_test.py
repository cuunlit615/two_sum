nums = [1,3,6,7,8,9]
# def twoSum(target):
l = []
n = len(nums)
numMap = {}
target =35

def twosum(target):
    for i in range(n):
        numMap[nums[i]] = nums[i]
    for i in range(n):
        num = numMap[nums[i]]
        if num < target:
            j = target - num
        else:
            print('nope')
            return False
        if j in numMap:
            print(j)
            p = num
            return p
        else:
            print('nope2')
            return False
print(twosum(7))
