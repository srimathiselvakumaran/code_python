num=int(input())
sum=0
count=0
temp=num
while temp>0:
  count=count+1
  temp=temp//10
temp=num
while temp>0:
  reminder=temp%10
  sum=sum+(reminder**count)
  temp//=10
if num==sum:
  print("yes")
else:
  print("no")
