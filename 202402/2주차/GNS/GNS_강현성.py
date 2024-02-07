import sys
sys.stdin = open('input.txt')

# 아이디어
# 1.각 요일이 나온 숫자를 카운트 하여 하나의 배열로 만든다.
# 2. 카운트 숫자만큼 요일을 반복적으로 result에 추가하여 출력을 만들어 준다.


T = int(input())
for tc in range(1,T+1):
    Test, N = input().split()
    N = int(N)
    arr = [input().split()]

    c = [0] * 10  # 요일들 카운트 저장하는 배열

    a = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT' ,'NIN']

    # try:
    for i in range(len(a)):
        for j in range(N):
            if a[i] == arr[0][j]:
                c[i] += 1

    # c[i]번만큼 a[i]번을 result에 추가해준다.
    # 예시) 첫번째 c(n) = [700, 716, 719, 734, 679, 737, 674, 654, 724, 704]
    # 700번 만큼 ZRO를 result에 더해주면 된다.
    result = []
    for i in range(len(c)):    # c[i]번만큼 a[i]번을 result에 추가해준다.
        while c[i]!= 0:        # 예시) 첫번째 c(n) = [700, 716, 719, 734, 679, 737, 674, 654, 724, 704]
            result.append(a[i])
            c[i] -= 1

    result = ' '.join(result)  # [] 제거하고 ZRO ZRO ZRO ZRO ZRO... 형태로 만들어 준다.
    print(f'#{tc} {result}')



#------------------------------------------------------
#강사님이 적으신 코드도 참고용으로 적어놓습니다.

T = int(input())
for tc in range(1, T+1):
    tc, N = map(lambda X: int(x) if x.isdecimal() else x, input().split())
    data = sorted(input().split(), key=lambda x: text_to_decimal[x])
    print(f'{tc}', *data)
