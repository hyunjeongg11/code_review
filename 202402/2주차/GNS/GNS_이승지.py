# import sys
# sys.stdin = open("GNS_test_input.txt", "r")

word_number = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR":4,
               "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
# number_word = {v:k for k, v in word_number.items()}

T = int(input())
for _ in range(T):
    test_case, test_number = input().split()

    input_string = input().split()
    # word_number의 value 기준으로 input_string sorted!
    # 람다함수의 리턴값에 의해 정렬되겠징
    sorted_string = sorted(input_string, key=lambda x: word_number[x])
    print(f'{test_case} {" ".join(sorted_string)}')