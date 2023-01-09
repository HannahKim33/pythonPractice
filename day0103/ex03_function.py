# def sayHello():
#     print('Hello')
#
# sayHello()



# def sayHello(name):
#     print("Hello",name)
#
# sayHello("Kim")



#
# def add(a,b):
#     return a+b
#
# print(add(3,4))




# def max(a,b):
#     r=a
#     if b>r:
#         r=b
#     return r
#
# data =max(2,3)
# print(data)



# def max(a,b):
#     if(b>a):
#         a=b
#     return a
#
# data =max(2,3)
# print(data)



# def acc(n):
#     sum=0
#     for i in range(n+1):
#         sum+=i
#     return sum
#
# print(acc(10))


# def max(a,b,c,d):
#     max=a
#     max2=d
#     if b>a:
#         max=b
#     if c>d:
#         max2=c
#     if max2>max:
#         max=max2
#     return max

# def max4(a,b,c,d):
#     if b>a:        a=b
#     if c>a:        a=c
#     if d>a:        a=d
#     return a

# def max2(a,b):
#     if b>a: a=b
#     return a
#
# def max4(a,b,c,d):
#     return max2(max2(a,b),max2(c,d))
#
# print(max4(5,2,10,6))


# def printNumber(n):
#     for i in range(n+1):
#         print(i,end=' ')
#         if i%10==9:
#             print()
#
# printNumber(36)
#
# def addAndMulti(a,b):
#     add=a+b
#     multi=a*b
#     return add,multi
#
# # i,j=addAndMulti(2,3)
# # print(i,j)
#
# data=addAndMulti(2,3)   #packing
# print(data)
# print(type(data))       #tuple (5,6)
# i,j=data                #unpacking
# print(i,j)


# a=[1,3,2,4]
# # print(a)
# # print(type(a))
#
# b=[50,2,11,27]
# c=[22,5,30,12,44,111,520]
#
# def f(list):
#     sum=0
#     for i in list:
#         sum+=i
#     avg=sum/len(list)
#     list.sort()
#     min=list[0]
#     list.reverse()
#     max=list[0]
#     return sum,avg,max,min
#
# def info(list):
#     sum=0
#     max = list[0]
#     min = list[0]
#     for i in list:
#         sum+=i
#         if i>max:
#             max=i
#         if i<min:
#             min=i
#     avg=sum/len(list)
#     return sum,avg,max,min
#
# print(f(a))
# print(f(b))
# print(f(c))

