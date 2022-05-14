def d(num):
    d1=list()
    while num!=0:
        i=num%2
        num//=2
        d1.append(i)
    d1.reverse()
    return d1

num=int(input('enter num'))
s=d(num)
for i in s:
    print(i,end="")
