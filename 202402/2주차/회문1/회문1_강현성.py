import sys
sys.stdin = open('input.txt')


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, 11):
    N = 8
    K = int(input())
    arr = [input() for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N - K + 1):  # 범위는 전체 배열의 길이가 N일때, 최대로 순환가능한 경우가 N-K-1부터 시작한다면, K 길이만큼 슬라이싱할 경우 N-1까지 입니다.
            if arr[i][j:j + K] == arr[i][j:j + K][::-1]: # 회문 판별입니다. [::-1] 을 통해 단어를 뒤집을 수 있습니다.
                count += 1

    for j in range(N):
        for i in range(N - K + 1):
            # 세로열은 가로열처럼 슬라이싱이 힘듭니다. 그렇기에 k라는 요소를 추가적으로 하는 반복문을 추가해줍니다.
            column = ''.join(arr[k][j] for k in range(i, i + K)) # 이거 한줄이면 세로열도 가로열처럼 만들어 줍니다.
            if column == column[::-1]:
                count += 1

    print(f'#{tc} {count}')

#----------------------------------------------------------------------------

# column = ''.join(arr[k][j] for k in range(i, i + K)) 를 풀어서 쓴다면 다음과 같습니다.

# case1. 문자열
# column = ''
# for k in range(i, i + K):
#     column += arr[k][j]

# case2. 리스트
# column = []
# for k in range(i, i + K):
#     column.append(arr[k][j])
