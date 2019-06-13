s,c=(input().split())
s=int(s)
c=int(c)

p=0
for i in range(s+1,c):
  d=i
  p=0
  while(d>0):
    w=d%10
    d=d//10
    e=w**3
    p=p+e
    if(i==p):
      print(i,end=' ')
