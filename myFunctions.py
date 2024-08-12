import os

def hello():
    print("hello Diana")

def hello1(name):
    print(f"hello {name}")

def Addition(x,y):
    print(x+y)


def Addition2(x,y):
    return x+y

s=Addition2(5,3)
print(s)

def Commands(cmd):
    
    os.system(cmd)

Commands('pwd')


def ClearScreen():
    os.system('clear')