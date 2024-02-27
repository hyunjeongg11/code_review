for tc in range(1,11):
    N = int(input())
    fx = input()
    stack = []
    postfix = ''
    cal = []
    result= 0
    # 1. 후위표기식으로 변환
    for i in fx:
        # 스택 비었으면 연산자 넣고
        if not stack and i == '+':
            stack.append(i)
        # 스택에 이미 +가 있으면 빼고 추가
        elif stack and i == '+':
            postfix += stack.pop()
            stack.append(i)
        # 숫자이면 그냥 추가
        else:
            postfix += i
    # 스택에 남아있는 마지막 + 빼줘야되서 for~else 로 처리함
    else:
        postfix += stack.pop()

    # 2. 결과값 계산
    for i in postfix:
        # 숫자이면 스택에 넣고
        if i != '+':
            cal.append(int(i))
        # 연산자이면 스택의 숫자 두개 꺼내서 더하고 다시 넣음
        elif i == '+':
            num2 = cal.pop()
            num1 = cal.pop()
            cal.append(num1 + num2)

    if len(cal) == 1:
        result = cal.pop()


    print(f'#{tc} {result}')
