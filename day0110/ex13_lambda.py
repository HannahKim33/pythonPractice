# def hap(x,y):
#     return x+y
# print(hap(2,3))

# print((lambda x,y:x+y)(10,20))
#
# hap=lambda x,y:x+y
# print(hap(2,3))

# def power(a):
#     return a**2
#
# a=[0,1,2,3,4]
# b=[]
#
# for data in a:
#     b.append(power(data))
# print(b)

# 위 처럼 리스트의 요소들을 하나하나 함수에 넣어야 할 때, 함수를 정의하지 않고 람다식을 통해 아래처럼 나타낼 수 있다.
# map(함수,리스트) 한 후 list로 타입 캐스팅함

# a=[0,1,2,3,4]
# b=list(map(lambda x:x**2,a))
# print(b)

a=[0,1,2,3,4,5,6,7,8,9,10]
b=list(filter(lambda x:x%2==0 and x!=0, a))
print(a)
print(b)