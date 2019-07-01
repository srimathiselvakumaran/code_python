num1=int(input())
sum=0
count=0
temp1=num1
while temp1>0:
  count=count+1
  temp1=temp1//10
temp1=num1
while temp1>0:
  reminder=temp1%10
  sum=sum+(reminder**count)
  temp1//=10
if num1==sum:
  print("yes")
else:
  print("no")
