# 자연수 N과 정수 K가 주어졌을 때 이항계수(N 밑 K)를 구하는 프로그램을 작성하시오.

# 입력 : 첫째 줄에 N과 K가 주어진다.(1<=N<=10, 0<=K<=N)
# 출력 : (N 밑 K)를 출력한다.

n, k = map(int,input().split())

def factorial(num):
    result = 1
    for i in range(2, num+1):
        result *= i
    return result

print(factorial(n) // (factorial(n-k) * factorial(k)))