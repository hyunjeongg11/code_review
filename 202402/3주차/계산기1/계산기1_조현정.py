import sys
sys.stdin = open('input.txt')

T = 10

for test in range(1, T+1):
    nLen = int(input())    # input 연산코드 길이
    cal = input()          # input 연산코드
    operatorStack = []     # 연산자 넣을 스택
    postfix = ''
    for elem in cal:
        if elem.isdigit():  # 숫자일 때 post에 넣어줌
            postfix += elem
        else:
            if operatorStack:   # stack이 비어있지 않을 때
                postfix += operatorStack.pop()  # 연산자를 post에 넣고 스택에서 제거
            operatorStack.append(elem)  # 새로운 연산자 스택에 추가
    postfix += operatorStack.pop()   # 남아있는 연산자까지 다 넣어줌
    operandStack = []  # 연산하기 위한 스택
    for elem in postfix:
        if elem != '+':   # 숫자인 경우 스택에 추가
            operandStack.append(int(elem))
    while len(operandStack) >= 2:  # 스택에 숫자가 2개 이상있을 때까지만
        operandStack.append(operandStack.pop() + operandStack.pop()) # 두 값 더해줌
    print(f'#{test} ', end='')
    print(*operandStack)