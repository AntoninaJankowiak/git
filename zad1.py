#n=5
#m=7
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

def printRec():
    for i in range(m):
      
      for j in range(n):
        print(t[i][j],end="")
      print()
    print()
#zad 17.1

def recTangle(a,b,c,d,full):
    if(a>c):
        a,c=c,a
    if(b>d):
        b,d=d,b
    i=a
    j=b
    if(full):
     while(i<=c):   
        while(j<=d):
            t[i][j]='x'
            j+=1
        i+=1
        j=b
    else:
     while(i<=c):
         t[i][b]='x'
         t[i][d]='x'
         i+=1
     while(j<=d):
         t[a][j]='x'
         t[c][j]='x'
         j+=1
    printRec()
#później 17.4

def recE(N):
  j=1
  for i in range(N):
      for o in range(j):
          t[i][o]='x'
      j+=1
  print(recTangle)
