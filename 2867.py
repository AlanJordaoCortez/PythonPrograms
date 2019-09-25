t = int(input('type a number: '))
for i in range(t):
    x,y = map(int,input('type two numbers: ').split())
    n = str(x ** y)
    print(len(n))

