snum=int(input())
s1=1
s2=1
count=0
while(count<snum):
  print(s1, end=' ')
  s3=s1+s2
  s1=s2
  s2=s3
  count+=1

