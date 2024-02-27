for tc in range(1, 11):
    N = int(input())
    fx = input()
    stack = []
    postfix = ''
    cal = []
    result = 0

    # 1. 후위표기식으로 변환
    for i in fx:
        if i == '*':
            while stack and stack[-1] == '*':
                postfix += stack.pop()
            stack.append(i)
        elif i == '+':
            while stack :
                postfix += stack.pop()
            stack.append(i)
        else:
            postfix += i

    # 스택에 남아있는 마지막 연산자 빼줘야되서 for~else로 처리함
    else:
        while stack:
            postfix += stack.pop()

    # print(postfix)
    # 2. 결과값 계산
    for i in postfix:
        if i not in '+*':
            cal.append(int(i))
        else:
            num2 = cal.pop()
            num1 = cal.pop()
            if i == '+':
                cal.append(num1 + num2)
            elif i == '*':
                cal.append(num1 * num2)

    result = cal.pop()

    print(f'#{tc} {result}')
