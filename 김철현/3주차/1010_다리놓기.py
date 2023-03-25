import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
from math import factorial as f

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    print(f(m) // (f(m - n) * f(n)))