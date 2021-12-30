'''
문제 5

아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.
    *
   * *
  * * *
 * * * *
* * * * *

'''

for i in range(5):
    for j in range(5):
        if j<4-i:
            print(" ", end='')
        else:
            print("*", end=' ')
    print()


#선생님 버전
for j in range(5):
    for i in range(4-j):
        print(' ', end='')
    for i in range(j+1):
        print('*', end='')
    print("")