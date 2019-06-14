s=input()
d=0
for i in range(len(s)):
  if(s[i].isdigit() or s[i].isalpha() or s[i]==' '):
    continue
  else:
    d=d+1
print(d) 
