import sys
sys.stdin = open('input.txt')

T = 10

for test in range(1, T+1):
    N = int(input())
    passwords = list(map(int, input().split()))
    front, rear = 0, 7
    n = 1
    while True:
        if n > 5:
            n = 1
        rear = (rear + 1) % len(passwords)
        if passwords[front] - n <= 0:
            passwords[rear] = 0
            break
        else:
            passwords[rear] = passwords[front] - n
            front = (front + 1) % len(passwords)
            n += 1
    print(f'#{test}', end=' ')
    for _ in range(8):
        rear = (rear + 1) % len(passwords)
        print(passwords[rear], end=' ')
    print()
