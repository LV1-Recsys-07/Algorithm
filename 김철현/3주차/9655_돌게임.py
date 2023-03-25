import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


n = int(input())
if n % 2 == 0:
    print("CY")
else:
    print("SK")
