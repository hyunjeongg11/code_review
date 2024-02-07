# import sys
# sys.stdin = open('input.txt')

T = int(input())

num_dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
for _ in range(T):
    test, num = input().split()
    str_list = list(input().split())
    temp = []   # str_list를 순회하며 key값(ex. ZRO)을 넣을 임시 리스트

    for i in range(len(str_list)):
        # num_dict에서 str_list[i]를 키값으로 하는 value(숫자들)를 temp에 추가
        temp.append(num_dict.get(str_list[i]))
    temp.sort() # 오름차순으로 정렬

    # 숫자가 들어가있는 정렬된 temp 리스트에 key값을 다시 넣어줌
    for i in range(len(temp)):
        for key, value in num_dict.items():
            if temp[i] == value:
                temp[i] = key

    print(test)
    print(*temp)