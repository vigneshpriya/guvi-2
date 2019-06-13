d,f=input().split()
d=int(d)
f=int(f)
for i in range(d+1,f):
  if(i>0):
    for p in range(2,i):
      if(i%p==0):
        break
    else:
      print(i,end=' ')
  else:
    break
