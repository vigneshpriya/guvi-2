n,k=input().split()
p=int(n)
q=int(k)
g=0
arr = [int(x) for x in input().split()]
for i in range (0,q):
  g=g+arr[i]
print(g)
