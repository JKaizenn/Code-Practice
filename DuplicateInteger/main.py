
#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
nums_2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1]

def array_tester(nums):
    for i in nums:
        if nums.count(i) > 1:
            return True
    return False
print


print(array_tester(nums))