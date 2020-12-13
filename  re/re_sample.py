import re


'''
meta characters 
. ^ $ * + ? { } [ ] \ | ( )
'''

'''
문자 클래스 [ ]
* [a-zA-Z]
* [0-9]
* ^

\d - 숫자와 매치, [0-9]와 동일한 표현식이다.
\D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
\s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
\S - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
\w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
\W - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.

Dot(.) - 정규 표현식의 Dot(.) 메타 문자는 줄바꿈 문자인 \n을 제외한 모든 문자와 매치됨을 의미한다.
'''

'''
반복 : * + {m} {m,n} ?
* {0,~}
+ {1,~}
?--> {0,1}
'''

p = re.compile('ab*')


p = re.compile('[a-z]+')
# match
m = p.match("python")
print(m) # match

m = p.match("3 python")
print(m) # None

'''
p = re.compile(정규표현식)
m = p.match( 'string goes here' )
if m:
    print('Match found: ', m.group())
else:
    print('No match')
'''

# serch
m = p.search("python")
print(m)
m = p.search("3 python")
print(m)

#findall
result = p.findall("life is too short")
print(result)

#finditer
result = p.finditer("life is too short")
print(result)
for r in result: print(r)

# match method
'''
group()	매치된 문자열을 돌려준다.
start()	매치된 문자열의 시작 위치를 돌려준다.
end()	매치된 문자열의 끝 위치를 돌려준다.
span()	매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.
'''
m = p.match("python")
print( m.group() )
print( m.start() )
print( m.end() )
print( m.span() )

# meta Characters
'''
|, ^, $, \A, \Z,\b, \B
'''

# \b - 단어 구분자(Word boundary)이다. 보통 단어는 whitespace에 의해 구분된다.
p = re.compile(r'\bclass\b') # space_class_space
print(p.search('no class at all'))

#grouping - ()
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
print(m.group())

p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")

'''
group(인덱스)	설명
group(0)	매치된 전체 문자열
group(1)	첫 번째 그룹에 해당되는 문자열
group(2)	두 번째 그룹에 해당되는 문자열
group(n)	n 번째 그룹에 해당되는 문자열
'''
p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m.group(1))

'''
그루핑된 문자열 재참조하기 - \1
'''
p = re.compile(r'(\b\w+)\s+\1')
p.search('Paris in the the spring').group()

'''
그루핑된 문자열에 이름 붙이기
(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)

(\w+) --> (?P<name>\w+)
(?P<그룹명>...)
'''
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name"))

'''
전방 탐색(Lookahead Assertions)

긍정형 전방 탐색((?=...)) - ... 에 해당되는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
부정형 전방 탐색((?!...)) - ...에 해당되는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
'''
print('[Lookahead Assertions]---------------')
str = "http://google.com"
print(str)
p = re.compile(".+:")
m = p.search(str)
print(m.group())

# 긍정형 전방 탐색
# http: --> http
print('<<Positive>>')
p = re.compile(".+(?=:)")
m = p.search(str)
print(m.group())

'''
.bat 제외 --> .*[.](?!bat$).*$
'''

'''
문자열 바꾸기
'''
p = re.compile('(blue|white|red)')
s=p.sub('colour', 'blue socks and red shoes')
print(s)
# 1회만 ??
s = p.sub('colour', 'blue socks and red shoes', count=1)
print(s)


p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))

# function for sub

def hexrepl(match):
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
s = p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')
print(s)
#'Call 0xffd2 for printing, 0xc000 for user code.'

# Greedy vs Non-greedy
s = '<html><head><title>Title</title>'
print(len(s))
print(re.match('<.*>', s).span())
print(re.match('<.*>', s).group())
#<html><head><title>Title</title>

# --> non-greedy : ?
# *? - 가능한 한 가장 최소한의 반복을 수행하도록 도와주는 역할을 한다.
print(re.match('<.*?>', s).group())