import sys

sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    length = int(input())
    cal_string = input()

    stack = []
    top = -1
    postfix_notation = []

    isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
    icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}

    for token in cal_string:
        # 피연산자다
        if token.isdigit():
            postfix_notation.append(token)
        # 연산자다! 코드 넘 복잡하네 좀 고쳐보이소
        # 아직 안 고침 죄송
        else:
            # token을 처리할 때까지 while문 돌아요
            while True:
                # ')'이면 '('을 만날 때까지 빼야하니까 반복문에 넣었숨당
                if token == ')':
                    while isp[stack[top]] != '(':
                        postfix_notation.append(stack.pop())
                        top -= 1
                    # '('만나면 그건 빼기만 하고 다시 넣지는 않아요~
                    # token으로 받은 ')'은 스택에 넣을 필요 없으니까 break
                    stack.pop()
                    top -= 1
                    break
                # 바깥에 있는 게 우선순위가 높으면 token을 스택에 넣어요
                elif (stack and isp[stack[top]] < icp[token]) or not stack:
                    stack.append(token)
                    top += 1
                    break
                # 안에 있는 게 우선순위가 높으면 맨 끝에 걸 스택에서 빼요
                # 토큰 처리 안 했으니까 break는 안 합니다.
                else:
                    postfix_notation.append(stack.pop())
                    top -= 1
    # 그냥 오류가 날 상황이 있잖아요
    # 사용자가 입력을 잘 못 했다던가... 그럴 ㄸㅐ 예외 처리하도록 넣어놨숨다
    try:
        while top >= 0 and stack[top] in '+-*/':
            postfix_notation.append(stack[top])
            stack.pop()
            top -= 1

        if stack:
            raise Exception("잘못된 수식을 입력하셨습니다.")
    except Exception as e:
        print(e)

    # 연산자를 str로 처리하니까 그걸 계산하도록 딕셔너리에 람다 넣어서 썼습니다.
    operators = {'+': lambda x, y: int(x)+int(y), '-': lambda x, y: int(x)-int(y), '*' : lambda x, y: int(x)*int(y), '/': lambda x, y: int(x)//int(y)}
    for token in postfix_notation:
        if token.isdigit():
            stack.append(token)
            top += 1
        else:
            num2 = stack.pop()
            top -= 1
            num1 = stack.pop()
            top -= 1
            
            # 스택에는 모든 게 지금 str로 들어가 있으니까 일단 바꿔서 넣어줘요
            stack.append(str(operators[token](num1, num2)))
            top += 1
    try:
        print(f'#{test_case} {stack.pop()}')
        top -= 1

        if stack:
            raise Exception("잘못된 수식을 입력하셨습니다.")
    except Exception as e:
        print(e)
