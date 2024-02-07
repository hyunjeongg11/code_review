# import sys
# sys.stdin = open('input.txt')

for test in range(1, 11):
    length = int(input())   # 회문의 길이
    data = [list(input()) for _ in range(8)]
    cnt = 0 # 회문의 개수

    # 가로 단어 확인
    for x in range(8):
        for y in range(8 - length + 1):
            word = data[x][y:y+length]
            if word == word[::-1]:
                cnt += 1

    # 세로 단어 확인
    for x in range(8 - length + 1):
        for y in range(8):
            word = ''
            for i in range(length):
                word += data[x+i][y]
            if word == word[::-1]:
                cnt += 1

    print(f'#{test} {cnt}')
