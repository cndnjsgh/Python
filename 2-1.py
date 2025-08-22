a = 4
b = 5
# 더하기
print(a+b)
# 빼기
print(a-b)
# 나누기
print(a/b)
# 몫
print(a//b)
# 나머지
print(a%b)
# 곱하기
print(a*b)
# 제곱
print(a**b)

c ='cndnjsgh'
# 문자열 길이 구하기
print(len(c))

# 줄 바꾸기
d='cndnjsgh\ncndnjsgh'
print(d)

# 탭 추가
e='추원호\t추원호'
print(e)

# 문자열 연산
print(c+d+e)
f = 'cndnjsgh'
print(f*5)

# 문자열 인덱스
print(f[0])
print(f[-1])

# 문자열 슬라이싱
g = f[0:4]
print(g)
g = f[::-1]
print(g)
g = f[::2]
print(g)

# 문자열 포매팅
a = '나는 사과를 %d개 먹었다' % 3
print(a)
a = '나는 %s를 %d개 먹었다' % ('과자',3)
print(a)

# 문자열 포매팅 왼쪽 공백 채우기
a = '%10s' % 'hi'
print(a)
# 문자열 포매팅 오른쪽 공백 채우기
a = '%-10s' % 'hi'
print(a)

# 소수점 표현하기
a = '%0.4f' % 3.141592
print(a)
a = '%.4f' % 3.141592
print(a)

# format 함수를 사용한 포매팅
a = "나는 사과를 {0}개 먹었다".format(3)
print(a)
number = 10
day = "하루"
a = "나는 사과를 {0}개 먹고 {1}동안 아팠다".format(number,day)
print(a)
a = "나는 사과를 {num}개 먹고 {dayday}동안 아팠음".format(num=20,dayday='3일')
print(a)

# format 함수를 사용한 정렬
a = "{0:<10}".format("안녕")
print(a)
a = "{0:>10}".format("안녕")
print(a)
a = "{0:^10}".format("안녕")
print(a)

# format 함수를 사용한 공백 채우기
a = "{0:^^10}".format("안녕")
print(a)

# format 함수를 사용한 소수점 표현
a = 3.141592
b = "{0:0.4f}".format(a)
print(b)

# *f문자열 포매팅
name = "추원호"
age = 22
a = f"제 이름은{name}이며 나이는{age}입니다"
print(a)
a = f"제 나이는 내년에 {age+1}살이 됩니다"
print(a)
# f포매팅 정렬도 가능
a = f"{"hi":>10}"
print(a)
# f포매팅 공백채우기도 가능
a = f"{'hi':*^10}"
print(a)
# {}를 출력하고 싶다면 2번 사용
a = f"{{and}}"
print(a)

# 문자열에서 특정 문자 개수 새기
a = "추추추원호"
print(a.count('추'))

# 문자열에서 특정 문자 위치 알려주기 없으면 -1반환
a = "추추추추원호"
print(a.find('김'))

# 문자열에서 특정 문자 인덱스 위치 없으면 오류
a = "추원호"
print(a.index("호"))

# 문자열 삽입
a = ",".join('cndnjsgh')
print(a)
a = ",".join(['cndnjsgh','cndnjsgh','cndnjsgh','cndjsgh'])
print(a)

# 대소문자 변환
a = "HeLLo"
print(a.upper())
print(a.lower())

# 공백 지우기
a = " 안녕 "
print(a.lstrip())
print(a.rstrip())
print(a.strip())

# 문자열 바꾸기
a ="Life is too short"
print(a.replace("Life","cndnjsgh"))

# 문자열 나누기
print(a.split())