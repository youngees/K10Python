'''
아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해보세요. 
(힌트: 이중 루프 사용)

*****
*****
*****
*****

'''

str = "*"
for str in range(5):
    for str in range(5):
        print(str, end="")
    print()
print()

str = "*"
print(str * 5)
