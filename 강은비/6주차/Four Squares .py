import sys

n=int(sys.stdin.readline())
l=[5]*(n+1) #각 제곱수를 만들 수 있는 방법의 수 
l[0]=0
l[1]=1

for i in range(2, n+1):
    for j in range(1, int(i**0.5)+1):
        l[i]=min(l[i-j*j]+1, l[i])     #i보다 작은 제곱수 j*j와 i-j*j를 만들 수 있는 방법의 합 중 최소를 찾음

print(l[n])
