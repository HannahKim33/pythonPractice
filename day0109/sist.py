def add(a,b):
    print("__name__:",__name__)
    return a+b

def sub(a,b):
    return a-b

if __name__=="__main__":
    print(add(1,1))
    print(sub(1,1))