import numpy as np

def not_used():
    a=[10,20,30,40]
    b=np.array(a)
    c=np.arange(10,50,10)

    print(a)
    print(b)
    print(c)

def not_used2():
    #0으로 채워진 n개짜리의 배열을 만들어 준다. 배열의 요소는 실수.
    a=np.zeros(3)
    print(a)

    #데이터요소의 자료형이 정수인 배열을 만들어 준다.
    b=np.zeros(3,dtype=np.int32)
    print(b)

    #0으로 채워진 3행 4열의 2차원 배열을 만든다.
    c=np.zeros([3,2])
    print(c)

    #0으로 채워진 데이터의 자료형이 정수인 3행 4열의 2차원 배열을 만든다.
    d=np.zeros([3,4],dtype=np.int32)
    print(d)

def not_used3():
    #1로 채워진 3개짜리 배열을 만들어 준다. 실수
    a=np.ones(3)
    print(a)

    #1로 채워진 3행 4열의 정수 배열
    b=np.ones([3,4],dtype=np.int32)
    print(b)

    #2로 채워진 3개짜리 배열
    #full(크기, 값)
    c=np.full(3,2)
    print(c)

    d=np.full(3,2.0)
    print(d)

def not_used4():
    #0부터 12-1까지 1씩 증가하는 요소를 갖는 1차원 배열
    a=np.arange(12)
    print(a)

    #1부터 10까지 1씩 증가하는 요소를 갖는 1차원 배열
    b=np.arange(1,11,1)
    print(b)

    c=np.arange(0,1,0.1)
    print(c)

    d=np.arange(10,0,-1)
    print(d)

def not_used5():
    a=np.arange(12)
    print(a)

    #배열의 차원을 바꾸기 위해 reshape 함수를 이용
    b=a.reshape(3,4)
    print(b)

    #numpy 배열의 차원과 행,열의 수 확인하기
    print(a.shape)
    print(b.shape)

    #-1은 알아서 해달라는 뜻. 열의 수만 4로 지정.
    c=a.reshape(-1,4)
    print(c)

    d=a.reshape(2,-1)
    print(d)

def not_used6():
    a=[10,20,30,40,50]
    b=np.array(a)
    tot=np.sum(b)
    print(tot)
    tot2=np.sum(a)
    print(tot2)

def not_used7():
    a=np.arange(12).reshape(3,-1)
    print(a)

    sum=np.sum(a)   #2차원 배열의 모든 원소의 값을 더하기
    sum0=np.sum(a,axis=0)    #axis=축. axis=0이면 수직. 같은 열의 요소들을 더하기 해서 열의 수와 동일한 1차원 배열이 만들어진다.
    sum1=np.sum(a,axis=1)   #수평으로 더하기
    print(sum)
    print(sum0)
    print(sum1)

def not_used8():
    a=np.arange(12).reshape(3,-1)
    print(a)
    max=np.max(a)           #전체 요소중에 제일 큰 값
    max0=np.max(a,axis=0)   #수직으로 제일 큰 값
    max1=np.max(a,axis=1)   #수평으로 제일 큰 값
    print(max)
    print(max0)
    print(max1)

def not_used9():
    a=np.arange(12).reshape(3,-1)
    print(a)
    b=np.cumsum(a,axis=0)           #배열의 원소들을 수직으로 누적하여 합을 만들어 준다   2차원 배열
    c=np.cumsum(a,axis=1)           #배열의 원소들을 수평으로 누적하여 합을 만들어 준다   2차원 배열
    d=np.cumsum(a)                  #모든 원소들을 차례로 누적해서 1차원 배열로 만들어 준다.
    e=d.reshape(-1,4)               #d를 다시 2차원 배열으로 만들기
    print(b)
    print(c)
    print(d)
    print(e)

def not_used10():
    a=np.arange(12).reshape(3,-1)
    print(a)

    #a배열과 동일한 shape의 0으로 채워진 배열을 만들기
    b=np.zeros_like(a)
    print(b)

    #a 배열과 동일한 shape의 1로 채워진 배열 만들기
    c=np.ones_like(a)
    print(c)

    #a 배열과 동일한 shape의 100으로 채워진 배열 만들기
    d=np.full_like(a,100)
    print(d)

def not_used11():
    a=np.arange(12)
    print(a)
    b=a[0]          #indexing(특정 자리의 값을 가져오기)
    print(b)
    print(type(b))

    c=a[0:3]        #특정 범위의 값들을 갖고 오기 (slicing)     반환하는 것은 넘파이배열
    print(c)
    print(type(c))

    d=a[:3]         #맨 처음 요소부터 갖고 올 때는 : 앞 부분 생략 가능
    print(d)

    e=a[5:]         #맨마지막도 생략 가능
    print(e)

    f=a[:]          #전부다
    print(f)

    g=a[::-1]       #거꾸로 뒤집어서 갖고 오기
    print(g)

    h=a[::2]        #짝수번째만
    print(h)

    i=a[1::2]       #홀수번째만
    print(i)

def not_used12():
    a=np.arange(12)
    print(a)
    # a[0]=-1             #인덱싱으로 값을 바꾸기
    # a[:3]=-1                #슬라이싱으로 값을 바꾸기
    # a[:]=-1           #모두
    a[1::2]=-1          #짝수번째만
    print(a)

def not_used13():
    a=np.arange(20).reshape(-1,4)
    print(a)
    # b=a[0][0]     #첫 번째 요소
    # b=a[1][2]
    # b=a[-1][-1]   #맨 마지막 원소
    # b=a[0]          #0번째 행
    # b=a[1:3]        #1~2행
    # b=a[3:]           #3~끝행
    b=a[::-1]          #행을 거꾸로 출력
    print(b)

def not_used14():
    a=np.arange(12).reshape(-1,4)
    # b=a[:,1]
    # print(b)
    # c=a[1:,1:3]
    # print(c)
    # print(a)
    # print(a[::-1])
    # print(a[0,0])
    # print(a[:2,0])
    # print(a[:2,:1])
    # print(a[:2,:2])
    # print(a[:,-1])
    # print(a[::-1][::-1])    #행을 거꾸로 했다가 다시 거꾸로->원래대로 돌아감
    # print(a[::-1,::-1])     #행도 열도 거꾸로
    #
    # print(a[:,0])
    # print(a[:,1])

    print(a)

    # b=np.zeros([4,3],dtype=np.int32)
    # print(b)
    # # b[0]=a[:,0]
    # # print(b)
    #
    # # for i in range(len(a[0])):
    # #     b[i]=a[:,i]
    # for i in range(a.shape[-1]):
    #     b[i]=a[:,i]
    # print(b)

    #행과 열을 바꿔주는 함수
    print(a.transpose())



def not_used15():
    a=np.arange(12).reshape(-1,4)
    print(a)
    # a[:] =-1
    # a[:,0]=9
    # print(a)

    b=a>5
    print(b)

    c=a[b]
    print(c)

    d=a[a>5]    #bool array
    print(d)

# a = np.arange(20).reshape(-1, 4)
# print(a)
# # print(a[1])
# # print(a[1,2])       #1행 2열의 요소 하나
# # print(a[[1,3]])     #[] 하나 더 치면 1행과 3행을 가져옴     index array
# # print(a[[1,3,4]])
#
# a[:]=-1
# a[0]=9
# print(a)

# a=np.zeros([5,5],dtype=np.int32)
# print(a)
# a[[0,-1]]=1
# # a[:,0]=1
# # a[:,-1]=1
# a[:,[0,-1]]=1
# print(a)
#
# b=np.ones([5,5],dtype=np.int32)
# print(b)
# b[1:-1,1:-1]=0
# print(b)

# a=np.zeros([5,5],dtype=np.int32)
# print(a)



# for i in range(len(a[1])):
#     a[i,i]=1
# print(a)

# a[[1,2,3,4],[1,2,3,4]]=1
# a[range(5),range(5)]=1
# print(a)
#
#
# b=np.zeros([5,5],dtype=np.int32)
# for i in range(len(b[1])):
#     b[i, len(b[1])-i-1] = 1
# print(b)

# d=[1,3,0,3,1]
#
# a=np.zeros([len(d),max(d)+1],dtype=np.int32)
# print(a)
#
# # for i in range(len(d)):
# #     a[i,d[i]]=1
#
# a[[0,1,2,3,4],[1,3,0,3,1]]
# a[range(len(d)),d]=1
# print(a)

# a=np.array([3,1,2])
# print(a)
# a.sort()    #배열 자신을 정렬해 줌. 배열 자체가 변함. 반환값 없음.
# print(a)
#
# b=a.argsort()
# print(a)
# print(b)
# print(a[b])

a=np.array([4,3,1,5,2])
# b=np.argsort(a)
#
# print(a)
# print(b)
# print(a[b])

print(np.max(a))        #배열 중에 가장 큰 값을 찾아준다.
print(np.argmax(a))     #배열 중에 가장 큰 값이 있는 위치의 인덱스를 반환한다.
print(a[np.argmax(a)])  #argmax를 인덱스로 사용해 최대값 가져오기