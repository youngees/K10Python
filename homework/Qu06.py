'''
문제 6

아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.
* * * * *
 * * * *
  * * *
   * *
    *
'''

for i in range(5):
    for j in range(5):
        if j<i:
            print(" ", end='')
        else:
            print("*", end=' ')
    print()


#선생님 버전
for j in range(5):
    for i in range(j):
        print(' ', end='')
    for i in range(5-j):
        print('*', end='')
    print("")