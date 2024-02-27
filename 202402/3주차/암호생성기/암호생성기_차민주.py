import sys
sys.stdin = open('input.txt')

for test in range(1, 11):
    T = int(input())
    data = list(map(int, input().split()))
    while data[-1] != 0:    # data의 마지막 원소가 0이 나올 때까지
        for minus in range(1, 6):   # 감소 값: 1 ~ 5
            new = data.pop(0) - minus
            if new > 0:
                data.append(new)
            else:   # minus 값을 뺀 결과가 음수라면
                data.append(0)  # 마지막에 0 추가
                break
    print(f'#{test}', *data)