dic = {'name':'cndnjsgh', 'age': '22'}
print(type(dic))
a = {'a':[1,2,3]}
print(a)
a = {1: 'a'}

# 딕셔너리에 추가하기
a['cndnjsgh'] = '22살'
print(a)

# 요소 삭제하기
del a[1]
print(a)

# 딕셔너리에서 키를 사용해서 Value 얻기
grade = {'pey':10, 'julliet':99}
print(grade['julliet'])

# 주의사항
# 같은 키가 있으면 안됨
# 리스트가 키로 들어 오면 안됨

# Key 리스트 만들기
a = {'name': 'cndnjsgh', 'age': 22}
print(type(a.keys()))

# Value 리스트 만들기
print(a.values())

# key와 value 쌍으로 얻기
print(a.items())

# key value 모두 지우기
a.clear()
print(a)

# key로 value 얻기 
a = {'name': 'cndnjsgh', 'age': 22}
print(a.get('name',"값이 없습니다"))
# 직접 하는 것과 차이는 get함수는 없으면 None 반환

# 해당 key가 딕셔너리 안에 있는지 확인하기
print('name' in a)