n=input("input yourname")
file="layla.txt"
inf=open(file,'r')
outf=open("a.txt","w")
s=[line.rstrip().split('=') for line in inf]
inf.close()

b=0
for i in s:
    print(i[0])
    a=input()
    if a==i[-1]:
        b+=1
print(n)
print(b)

outf.write(n)
outf.write(str(b))
outf.close()
