a = 1
b = 2
c = 3

def shift():
    global a, b, c
    x = a
    a = b
    b = c
    c = x

while True:
    shift()
    print(a, b, c)
    input()