n1=input()
s1=0
for i in range(len(n1)):
  if(n1[i].isdigit() or n1[i].isalpha() or n1[i]==(" ")):
    continue
  else:
    s1+=1
print(s1)
