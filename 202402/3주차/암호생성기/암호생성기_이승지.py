from collections import deque
# import sys
# sys.stdin = open("input.txt", "r")

for _ in range(10):
    test_case = int(input())
    numbers = map(int, input().split())

    dq = deque(numbers)
    
    # 이중 반복문이라서....  탈출하려고 변수 하나 만들었슴둥
    search_continue = True
    while search_continue:
        for cnt in range(1, 6):
            first = dq.popleft()
            changed = first-cnt
            if changed < 0:
                changed = 0
            dq.append(changed)

            if changed == 0:
                search_continue = False
                break
    print(f'#{test_case} {" ".join(map(str, dq))}')