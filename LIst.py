e = [1, 2, 'list', 'is']
print(type(e))
print(e[1]+e[0]) 
print(e[2]+e[3])
print(e[-1])

# 리스트안에 리스트
a = [1,2,3,['a','b','c']]
print(a[3][-1])

# 리스트안에 문자열
a =[1,"hello",3,['a','b','c']]
print(a[1][-1])

# 슬라이싱
a =[1,2,3,4,5]
print(a[0::2])

a=[1,2,3,['a','b','c'],4,5]
print(a[2:5])

# 리스트 연산하기
a= [1,2,3]
b= [4,5,6]
print(a+b)
print(a*3)

# 리스트 길이구하기
print(len(a))

# 리스트 수정
a = [1,2,3]
a[2]=4
print(a)

del a[1]
print(a)

b= [4,5,6]
print(a[0]+b[0])

del b[1:]
print(b)

# 리스트에 요소 추가하기
a = [1,5,6,2,23,4]
a.append(7) 
print(a)
# 오름차순 정렬(알파벳도 가능(사전순))
a.sort()
print(a)

# 뒤집기
a.reverse()
print(a)

# 인덱스 반환(값 찾기)
print(a.index(23))

# 리스트에 삽입
a.insert(5,56)
print(a)

# 리스트 요소 제거(가장 먼저 잡힌 값)
a.remove(23)
print(a)

# 리스트 요소 끄집어 내기(괄호안에 있는 위치에 인덱스)
a = [1,2,3,4,5,6]
print(a.pop())

# 리스트에 포함된 요소 개수 새기
print(a.count(1))

# 리스트 확장
a = [1,2,3]
a.extend([4,5])
print(a)
a.append([4,5])
print(a)