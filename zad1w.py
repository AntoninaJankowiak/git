
n=5
m=5
t=[]
for i in range(m):
    x=[]
    for j in range(n):
        x.append('o')
    t.append(x)
for i in range(m):
    for j in range(n):
        print(t[i][j],end="")
    print()
