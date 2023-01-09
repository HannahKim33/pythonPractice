import re


'''
    따옴표 세 개->주석문
    re: regular expression (정규 표현식)
'''

# a='''12
# 34
# 56'''
# print(a)

db='''
3412    Bob 123
4567    Tom 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534
1234  Tiger 123
'''

ns=re.findall(r'[0-9]+',db)
print(ns)

print('-'*50)

names=re.findall(r'[A-Z][a-z]+',db)
print(names)

# phones=re.findall(r'\d{4}',db)
phones=re.findall(r'^\d+',db,re.MULTILINE)
print(phones)



# ids=re.findall(r'\d{3}',db)
ids=re.findall(r'\d+$',db,re.MULTILINE)
print(ids)


namet=re.findall(r'T[a-z]+',db)
print(namet)

# name_not_t=re.findall(r'[ABCDEFGHIJKLMNOPQRSUVWXYZ][a-z]+',db)
name_not_t=re.findall(r'[A-SU-Z][a-z]+',db)
print(name_not_t)

print(type(name_not_t))

for name in name_not_t:
    print(name)