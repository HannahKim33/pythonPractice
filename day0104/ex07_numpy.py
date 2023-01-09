import numpy




def notUsed():
    data=[1,5,8,2,6,9,0,4]
    print(data, type(data))

    data2=numpy.array(data)
    print(data2, type(data2))

    data3=data2+1   #각 원소에 1씩 더해줌. broad operation
    print(data3)

    # data4=data+1  #에러
    # print(data4)

    print(data2>5)
    print(data2[data2>5])   #Fancy indexing