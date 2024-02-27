import sys
sys.stdin = open('input.txt')

for test in range(1, 11):
    length = int(input())
    code = input()
    postfix = ''
    stack = []
    temp = []
    result = ''
    for i in range(length):
        if code[i] == '+' and stack:    # 연산자이고 스택에 뭐가 있는 경우
            postfix += stack.pop()
            stack.append(code[i])
        elif code[i] == '+' and not stack:  # 연산자이고 스택에 아무것도 없는 경우
            stack.append(code[i])
        else:   # 피연산자인 경우
            postfix += code[i]
    else:   # for문 다 돌고 나면 stack에 남아 있는 연산자 마저 pop
        postfix += stack.pop()

    for j in postfix:
        if j.isdecimal():
            temp.append(int(j))
        elif j == '+' and temp:
            b = temp.pop()
            a = temp.pop()
            result = a + b
            temp.append(result)
    print(f'#{test} {result}')
