n=int(input())
arr=list(map(int,input().split()[:n]))
arr.sort()
for i in arr:
  print(i,end=" ")
