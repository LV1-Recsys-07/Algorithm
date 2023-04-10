import sys

n=int(sys.stdin.readline())
nums=[int(sys.stdin.readline()) for _ in range(n)]
nums.sort(reverse=True)
print(sum([nums[i]-i  for i in range(n) if nums[i]>i]))