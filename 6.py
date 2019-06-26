year=int(input())
if y%4==0:
  print("yes")
elif year%100==0:
  print("no")
elif year%400==0:
  print("yes")
else:
  print("no")