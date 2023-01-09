# n=int(input('숫자: '))
# i=1
#
# while i<=n:
#     print("hello")
#     i+=1

# prompt='''
#     1.Add
#     2.Del
#     3.List
#     4.Quit
#     메뉴를 선택하세요 :
# '''
# number=0
# while number!=4:
#     print(prompt)
#     number=int(input())
#     if number==1:
#         print("등록했습니다")
#     elif number==2:
#         print("삭제했습니다")
#     elif number==3:
#         print("목록을 출력합니다")
# print("종료합니다")


# n=int(input("몇 단: "))
# i=1
# while i<=9:
#     print(n,'*',i,'=',n*i)
#     i+=1

n=int(input("수: "))
# mul=1
#
# while n>0:
#     mul*=n
#     n-=1
#
# print(mul)

r=1
i=n
while i>1:
    print(i,"*", end='')
    r*=i
    i-=1
print("1","=",r)