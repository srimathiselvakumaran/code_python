n1=input()
sum1=0
for i in range(len(n1)):
  if(n1[i].isdigit() or n1[i].isalpha() or n1[i]==(" ")):
    continue
  else:
    sum1+=1
print(sum1)
