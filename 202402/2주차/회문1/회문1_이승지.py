# import sys
# sys.stdin = open("input.txt", "r")

# 담부턴 전치행렬 써볼게욤..

for test_case in range(1, 11):
    length = int(input())
    area = [list(input()) for _ in range(8)]

    count = 0
    # 가로
    # 8행을 가지고 있으니까
    for i in range(8):
        # i행의 요소를 length개씩 슬라이싱 할 건데
        # 슬라이싱 되는 서브리스트의 첫번째 인덱스의 범위는 0부터 8-length+1
        for j in range(8-length+1):
            # i행의 j번째 요소들을 length개씩 슬라이싱
            target_list = area[i][j:j+length]
            # 그걸 뒤집은 리스트
            reverse_list = target_list[::-1]

            # 같냐? 같으면 count ++
            if target_list == reverse_list:
                count += 1
    # 세로
    # j열의 요소를 length개씩 슬라이싱 할 건데
    # 슬라이싱 되는 서브리스트의 첫번째 인덱스의 범위는 0부터 8-length+1
    for j in range(8):
        for i in range(8-length+1):
            # j열의 요소들을 슬라이싱 할 건데 행 단위로 요소들이 들어가 있으니까
            # 행을 length개씩 방문하며 해당 행의 j번째 열의 요소를 list에 넣는다
            target_list = [area[k][j] for k in range(i, i+length)]
            # 그걸 뒤집은 리스트
            reverse_list = target_list[::-1]

            # 같으면 count ++
            if target_list == reverse_list:
                count += 1

    print(f'#{test_case} {count}')
