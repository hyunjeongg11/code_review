# import sys
# sys.stdin = open("input.txt", "r")
 
t = 10
 
operators = {"+": lambda x, y: x + y,
             "-": lambda x, y: x - y,
             "*": lambda x, y: x * y,
             "/": lambda x, y: x // y}
 
def push(stack, char):
    stack.append(char)
 
def isEmpty(stack):
    if(len(stack) == 0):
        return True
    return False
 
def top(stack):
    if(isEmpty(stack)):
        return None
    return stack[-1]
 
def makePostfix():
    postfixList = []
    operatorStack = []
    for char in myStr:
        if(char.isdecimal()):
            postfixList.append(char)
            continue
        if(char == "("):
            push(operatorStack, char)
            continue
        if(char == ")"):
            while(isEmpty(operatorStack) == False and top(operatorStack) != "("):
                postfixList.append(top(operatorStack))
                operatorStack.pop()
            operatorStack.pop()
            continue
        if(char == "*" or char == "/"):
            while(isEmpty(operatorStack) == False and (top(operatorStack) == "*" or top(operatorStack) == "/")):
                postfixList.append(top(operatorStack))
                operatorStack.pop()
        else:
            while(isEmpty(operatorStack) == False and top(operatorStack) != "("):
                postfixList.append(top(operatorStack))
                operatorStack.pop()
        push(operatorStack, char)
 
    while(isEmpty(operatorStack) == False):
        postfixList.append(top(operatorStack))
        operatorStack.pop()
 
    postfixStr = "".join(postfixList)
    return postfixStr
 
def calPostfix(postfixStr):
    numStack = []
    for char in postfixStr:
        if(char.isdecimal()):
            push(numStack, int(char))
        elif(char in operators):
            operand2 = top(numStack)
            numStack.pop()
            operand1 = top(numStack)
            numStack.pop()
            result = operators[char](operand1, operand2)
            push(numStack, result)
    return top(numStack)
 
def solve(tc):
    postfixStr = makePostfix()
    answer = calPostfix(postfixStr)
    print(f"#{tc} {answer}")
 
for tc in range(t):
    strLen = int(input())
    myStr = input()
    solve(tc+1)