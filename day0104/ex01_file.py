# f=open("hello.txt","w",encoding="UTF-8")
# f.write("안녕하세요\n")
# f.write("반갑습니다.")
# f.close()
# print("파일이 생성되었습니다.")

# f=open("hello.txt","w",encoding="UTF-8")
# f.write("hello 파이썬")
# f.close()
# print("OK")

# f=open("hello.txt","a",encoding="UTF-8")
# f.write("hello mongo")
# f.close()
# print("OK")
#
# f=open("./Data/out.txt","w",encoding="UTF-8")
# for i in range(1,11):
#     data="%d번째 줄입니다.\n" %i
#     f.write(data)
# f.close()
# print("OK")

f=open("./Data/gugudan.txt","w",encoding="UTF-8")
for i in range(2,10):
    f.write("%d단\n" %i)
    for j in range(1,10):
        f.write("{0} * {1} = {2}\n".format(i,j,i*j))
    f.write("\n")
f.close()
print("OK")