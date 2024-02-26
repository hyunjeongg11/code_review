import sys
sys.stdin = open('input.txt')

T = 10

for test in range(1, T+1):
    nLen = int(input())
    cal = input()
    operatorStack = []
    postfix = ''
    for elem in cal:
        if elem.isdigit():
            postfix += elem
        elif elem == '*':
            while operatorStack and operatorStack[-1] == '*':
                postfix += operatorStack.pop()
            operatorStack.append(elem)
        else:
            while operatorStack:
                postfix += operatorStack.pop()
            operatorStack.append(elem)
    while operatorStack:
        postfix += operatorStack.pop()
    operandStack = []
    for elem in postfix:
        if elem.isdigit():
            operandStack.append(int(elem))
        elif elem == '*':
            operandStack.append(operandStack.pop()*operandStack.pop())
        else:
            operandStack.append(operandStack.pop()+operandStack.pop())

    print(f'#{test} ', end='')
    print(*operandStack)