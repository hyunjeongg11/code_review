import sys
sys.stdin = open('input.txt')

def make_postfix(code): # 후위표기식 만드는 함수
    postfix = ''
    stack = []
    for tk in code:
        if tk == '*':
            while stack and stack[-1] == '*':   # stack의 top에 *보다 연산순위가 낮은 게 올 때까지 pop
                postfix += stack.pop()
            stack.append(tk)
        elif tk == '+':
            while stack: # stack이 비어질 때까지
                postfix += stack.pop()   # postfix에 pop한 값 넣어주고
            stack.append(tk) # + 연산자는 stack에 추가
        else:  # 피연산자라면
            postfix += tk
    while stack:   # for문 다 돌면 stack에 나머지 연산자도 pop
        postfix += stack.pop()
    return postfix

def calculate(fx):  # 후기표기식 계산하는 함수
    stack = []
    for i in fx:    # 후위표기식 순회하면서
        if i.isdecimal():   # 숫자일 경우
            stack.append(int(i))    # stack에 추가
        elif i in '*+' and stack:
            b = stack.pop()
            a = stack.pop()
            if i == '*':
                stack.append(a * b)
            elif i == '+':
                stack.append(a + b)
    return stack.pop()

for test in range(1, 11):
    length = int(input())
    code = input()
    result = calculate(make_postfix(code))
    print(f'#{test} {result}')
