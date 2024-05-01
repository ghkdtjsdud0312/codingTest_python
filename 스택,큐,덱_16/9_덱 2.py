# 정수를 저장하는 덱을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# 명령은 총 여덟 가지이다.
# 1 X: 정수 X를 덱의 앞에 넣는다. (1 ≤ X ≤ 100,000)
# 2 X: 정수 X를 덱의 뒤에 넣는다. (1 ≤ X ≤ 100,000)
# 3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 5: 덱에 들어있는 정수의 개수를 출력한다.
# 6: 덱이 비어있으면 1, 아니면 0을 출력한다.
# 7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다.
# 8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다.

# 입력 : 첫째 줄에 명령의 수 N이 주어진다. (1 ≤ N ≤ 1,000,000)
# 둘째 줄부터 N개 줄에 명령이 하나씩 주어진다.
# 출력을 요구하는 명령은 하나 이상 주어진다.
# 출력 : 출력을 요구하는 명령이 주어질 때마다 명령의 결과를 한 줄에 하나씩 출력한다.

import sys
from collections import deque
n = int(input())

dequeue = deque()
for i in range(n):
    num = list(map(int, sys.stdin.readline().strip().split()))
    l = len(dequeue)
    if num[0] == 1:
        dequeue.appendleft(num[1])
    elif num[0] == 2:
        dequeue.append(num[1])
    elif num[0] == 3:
        print(dequeue.popleft() if l else -1)
    elif num[0] == 4:
        print(dequeue.pop() if l else -1)
    elif num[0] == 5:
        print(len(dequeue))
    elif num[0] == 6:
        print(0 if l else 1)
    elif num[0] == 7:
        print(dequeue[0] if l else -1)
    elif num[0] == 8:
        print(dequeue[-1] if l else -1)