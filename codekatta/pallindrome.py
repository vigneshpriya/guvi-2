o=int(input())
s=o
h=0
while(o>0):
    d=o%10
    h=h*10+d
    o=o//10
if( s==h):
    print("yes")
else:
    print("no")
