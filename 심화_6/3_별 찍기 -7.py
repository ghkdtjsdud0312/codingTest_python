# 입력 : 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 출력 : 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

n = int(input())
for i in range(1,n):
    print(' '*(n-i) + '*'*(2*i-1))
for i in range(n,0,-1):
    print(' '*(n-i) + '*'*(2*i-1))