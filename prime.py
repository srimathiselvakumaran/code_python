s=int(input())
if s>1:
  for i in range(2,s):
    if s%i == 0:
      print("no")
      break
  else:
    print("yes")
else:
  print("no")
