num =int(input())
sum=0
if(num!=0):
	dig=num%10
	cube=dig*dig*dig
	sum=sum+cube
	num=num/10
	print("yes")
else:
	print("no")
