a=[1,3,5,7,9,0,2,4,6,8]

print(a[0:len(a)//2], a[len(a)//2:len(a)])
#처음 시작 0은 생략 가능
#맨끝까지 슬라이싱 할 경우 콜론 뒤 부분 생략 가능
print(a[:len(a)//2])
print(a[len(a)//2:])
print("-"*50)
print(a[0:-1])
print(a[:]) #전부다
print(a[0:len(a):1])


print(a[0::2])
print(a[::2])

print(a[-1::-1])
print(a[::-1])  #위와 같은 결과. -1 생략 가능

print(a[-1::-2])
print(a[::-2])  #위와 같은 결과. -1 생략 가능

print(a[-2::-2])

print("-"*50)

b=a     #얕은 복사, shallow copy
c=a.copy()      #깊은 복사
d=a[:]          #깊은 복사

a[0]=100
print("a:",a)   #a의 요소를 변경하면 b도 변경됨
print("b:",b)
print("c:",c)
print("d:",d)