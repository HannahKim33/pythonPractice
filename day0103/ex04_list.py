# collection: list  tuple   set     dictionary
#              []      ()    {}      {}
# tuple: 리스트의 상수 버전 (변경 불가능)

# a=[1,3,5,7]
# print(a)
# print(a[0],a[1],a[2])
# print(len(a))
#
# for i in range(len(a)):
#     print(i,a[i])

# a.reverse()
# print(a)

# b=[]
# for i in range(len(a)):
#     index=len(a)-1-i
#     b.append(a[index])
# a=b
# print(a)
# print('-'*50)
# for i in range(len(a)-1,-1,-1):
#     print(i,a[i])
#
# for i in reversed(range(len(a))):
#     print(i,a[i])
#
# print('-'*50)
#
# for i in a:
#     print(i, end=' ')
#
# for i in reversed(a):
#     print(i, end=' ')
#
# print()
# print(reversed(a))      #이 자체는 리스트가 아님. list() 해줘야 리스트가 됨
# print(list(reversed(a)))
#
# print('-'*50)
# a=[1,3,5]
# b=(1,3,5)
# print(a, type(a))
# print(b, type(b))


a=[1,2,3,4,1,2]
b=(1,2,3,4,1,2)
c={1,2,3,4,1,2}
print(a,type(a))
print(b,type(b))
print(c,type(c))    #{1, 2, 3, 4}   <= set은 중복을 허용하지 않음

b=list(b)
print(b,type(b))
b[0]=100
print(b)
#tuple을 리스트로 바꾸면 원소를 변경 가능

b=tuple(b)
print(b,type(b))
#list로 바꾼 tuple을 다시 tuple로 바꿀 수 있음

print('-'*50)
data=[3,5,1,3,5,1,3,5,1,3,5,1]

data=list(set(data))
print(data)

print('-'*50)

a=[100,90,80]
b={'kor':100,'eng':90,'math':80}    #dictionary. 자바의 map과 비슷
print(b,type(b))

print(a[0])
print(b['kor'])
print(b.keys())     #dict_keys(['kor', 'eng', 'math'])
print(b.values())   #dict_values([100, 90, 80])
print(b.items())    #dict_items([('kor', 100), ('eng', 90), ('math', 80)])  =>tuple

for i in b.keys():
    print(i, b[i])
print()
for i in b.values():
    print(i)
print()
for i,j in b.items():
    print(i, j)
for i in b.items():
    print(i,i[0],i[1])

print('-'*50)

for i in b:
    print(i)