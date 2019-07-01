num =int(input())
temp=num
sum=0
while(num!=0):
	dig=num%10
	cube=dig*dig*dig
	sum=sum+cube
	num=num//10
if(temp==num):
	print("yes")
else:
	print("no")
