# def compareNumber(a,b):
#     if(a>b):
#         return a
#     elif(a<b):
#         return b
#     else:
#         return '두 수가 같음'
#
# re='Y'
# while re!='N':
#     a=int(input("첫번째 수:"))
#     b=int(input("두번째 수:"))
#     print('큰 수:',compareNumber(a,b))
#     re=input('계속? (Y/N) ')




#
# def factorial(n):
#     mul=1
#     str='{0}!='.format(n)
#
#     while n>1:
#         str+='{0}*'.format(n)
#         mul*=n
#         n-=1
#
#     str+='1'+'={0}'.format(mul)
#     return str
#
# print(factorial(int(input("수: "))))


def gugudan(n):
    i=1
    str=''
    while i<=9:
        str+='{0}*{1}={2}\n'.format(n,i,n*i)
        i+=1
    return str
print(gugudan(int(input("몇 단?: "))))