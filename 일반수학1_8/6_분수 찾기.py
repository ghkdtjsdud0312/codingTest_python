# 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

# 입력 : 첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.
# 출력 : 첫째 줄에 분수를 출력한다.


num = int(input())
line = 1

while num > line:
    num -= line
    line += 1

# 짝수일경우
if line % 2 == 0:
    a = num
    b = line - num + 1
# 홀수일경우
elif line % 2 == 1:
    a = line - num + 1
    b = num

print(f'{a}/{b}')