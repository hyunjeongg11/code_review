import sys

sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    length = int(input())
    cal_string = input()

    stack = []
    top = -1
    postfix_notation = []

    isp = {'(': 0, '+': 1, '-': 1, ('*', '/'): 2}
    icp = {'(': 3, '+': 1, '-': 1, ('*', '/'): 2}

    for token in cal_string:
        if token.isdigit():
            postfix_notation.append(token)
        else:
            while True:
                if token == ')':
                    while isp[stack[top]] != '(':
                        postfix_notation.append(stack.pop())
                        top -= 1
                    stack.pop()
                    top -= 1
                    break
                elif (stack and isp[stack[top]] < icp[token]) or not stack:
                    stack.append(token)
                    top += 1
                    break
                else:
                    postfix_notation.append(stack.pop())
                    top -= 1
    try:
        # 이 부분말고 계산기2랑 똑같이 했어요
        # 2가 더 정확합니다 ㅎㅎ 그거 봐주세욤
        if stack[top] in '+-/%':
            postfix_notation.append(stack[top])
        stack.pop()
        top -= 1

        if stack:
            raise Exception("잘못된 수식을 입력하셨습니다.")
    except Exception as e:
        print(e)

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

            stack.append(str(operators[token](num1, num2)))
            top += 1
    try:
        print(f'#{test_case} {stack.pop()}')
        top -= 1

        if stack:
            raise Exception("잘못된 수식을 입력하셨습니다.")
    except Exception as e:
        print(e)
