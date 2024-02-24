# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    stack = []
    input_string = input()

    for element in input_string:
        if len(stack) == 0 or stack[-1] != element:
            stack.append(element)
        else:
            stack.pop()
    print(f'#{test_case} {len(stack)}')
