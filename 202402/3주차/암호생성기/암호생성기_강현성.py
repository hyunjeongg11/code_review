from collections import deque

for tc in range(1,11):
    T = int(input())
    password = list(map(int,input().split()))
    # print(password)
    queue = deque()
    rear = -1
    while rear < len(password) - 1:
        rear += 1
        queue.append(password[rear])
    # print(queue)

    while queue[-1] != 0 :
        for i in range(1,6):
            a = queue.popleft()
            b = a - i
            if b <= 0:
                b = 0
                queue.append(b)
                break
            else:
                queue.append(b)

    print(f'#{tc} {" ".join(map(str, queue))}')

