'''
아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해보세요. 
(힌트: 이중 루프 사용)

*****
*****
*****
*****

'''

for i in range(4):
    print("*" *5)


#선생님 버전
for j in range(4):
    for i in range(5):
        print('*', end='')
    print("")