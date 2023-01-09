n=int(input('숫자: '))
# if(n%2==0):
#     print("짝수")
# else:
#     print("홀수")
# if n%2:
#     print("홀수")
# else:
#     print("짝수")
# 
# if n==0:
#     print('0')
# elif (n>0):
#     print("양수")
# else:
#     print("음수")

if n>=0:
    if n<10:
        print("한자리 수")
    elif n<100:
        print("두자리 수")
    elif n<1000:
        print("세자리 수")
    else:
        print("네자리 수")
else:
    print("양수를 입력하세요")