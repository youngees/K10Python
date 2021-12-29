'''
파일명 : 02List.py

파이썬에는 연속된 Collection 데이터 구조에 
list, tuple, dictionary, set 이 있다.

리스트(list)
    : 대괄호[] 안에 콤마로 항목을 구분하며, 대입연산자로 항목을 변경할 수 
    있는 시퀀스 자료형이다. 서로 다른 자료형의 항목으로도 구성할 수 있다.
    인덱싱, 슬라이싱, 연결, 반복 등이 가능하다.
'''
# 기본적인 선언과 사용법은 배열과 동일하다. 
# 선언
list1 = [1,2,3,4,5]
list2 = ['Java', 'HTML', 'Python']
# 중첩된 리스트 선언 
list3 = [10,20, ['Java','HTML','Python']]

# 출력
print('list1:', list1) # 리스트 전체가 출력됨
print('list2[2]:', list2[2]) 
print('list3[2]:', list3[2]) # 리스트 내의 리스트가 출력됨

# 리스트 슬라이싱
print("===슬라이싱", "="*30)
print('list1[1:4]:', list1[1:4]) # 1~3까지 출력
print('list1[:3]:', list1[:3]) # 0~2까지 출력
print('list1[1:]:', list1[1:]) # 1~마지막까지 출력 

# 리스트 연결 
print("===리스트 연결", "="*30)
# 리스트 내에 또 다른 리스트를 삽입하여 연결하는 형태
all_list = [list1, list2]
print('all_list:', all_list)
print('all_list[1][0]:', all_list[1][0]) # java 출력됨

print("===list관련 메소드", "="*30)
list1.append(6)
print('append(6)=>',list1)

list1.clear()
print('clear()=>', list1)

list1.extend([10,20,30,40,50])
print('extend=>',list1)
list1.insert(1,99)
print('insert=>', list1)

print(list1.pop())
print('pop()=>',list1)

list1.remove(99)
print('remove=>', list1)

list1.reverse()
print('reverse()=>', list1)

print("===List Compreshension", "="*30)
list = [n ** 2 for n in range(10) if n%3==0]
print(list)