'''
문제 8

아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성 해보세요.
*********
 *******
  *****
   ***
    *
'''

for i in range(5):
    for j in range(9):
        if j<i:
            print(' ', end='')
        elif j<9-i:
            print("*", end='')
    print()
            