nums = []
for i in range(3):
    nums.append(int(input()))
nums = sorted(nums)
d = nums[1] - nums[0]
print(nums[0] - d)
print(nums[2] + d)