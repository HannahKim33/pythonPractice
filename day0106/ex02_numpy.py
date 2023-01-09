import numpy as np

# a=np.arange(5)
# print(a)
# print(list(a))
# print(type(a))
#
# print(np.arange(10))
# print(np.arange(10,20))
# print(np.arange(10,20,2))   #시작값, 종료값, 증감식
# print(np.arange(5,-5,-1))
#
# a=np.arange(5)
# print(a.shape)  #->(5,) ->1차원, 데이터 5개
# print(a.ndim)   #1 -> 차원을 알려줌
# print(a.dtype)  #int32 -> 데이터 타입 알려줌
#
# b=np.arange(6).reshape(2,-1)
# print(b)
# print(b.shape, b.ndim, b.dtype)
#
# print(a.size, b.size)           #배열 원소 개수
# print(a.itemsize,b.itemsize)    #자료형의 크기
# print(len(a),len(b))            #1차원 배열은 size와 똑같음. 원소의 개수. 2차원 배열일 때에는 행의 크기.
# print(len(b[0]))                #열의 개수
#
# print([1,3,5])
# print(np.array([1,3,5]))

#0-5까지의 정수가 들어 있는 2행 3열 넘파이 배열 만들기 (세 가지 방식으로)
# print(np.array([[0,1,2],[3,4,5]]))
# print(np.arange(6).reshape(2,3))
# print(np.arange(6).reshape(2,-1))
# print(np.arange(6).reshape(-1,3))
# print(np.array(range(6)).reshape(2,-1))
# print(np.array([range(3),range(3,6)]))
#
# print('-'*50)

#2차원 배열을 1차원 리스트로 만들어보기
# a=np.arange(6).reshape(2,3)
# print(a)
# b=a.reshape(a.size)
# print(b)

# a=np.array([1,2,3])
# r=a+10              #각 원소에 10을 더해줌
# print(r)
#
# b=np.array([4,5,6])
# r2=a+b          #[5,7,9]   => vector operation: 배열의 길이가 같을 때 각 자리의 원소끼리 연산
# print(r2)

a=np.arange(3)
b=np.arange(6)
c=np.arange(3).reshape(-1,3)
d=np.arange(6).reshape(-1,3)
e=np.arange(3).reshape(3,-1)
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
#
# print(a.shape, a.ndim, a.size)
# print(b.shape, b.ndim, b.size)
# print(c.shape, c.ndim, c.size)
# print(d.shape, d.ndim, d.size)
# print(e.shape, e.ndim, e.size)

#5개의 변수에 대해 각각 덧셈을 실행하기
