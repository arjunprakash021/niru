n=int(input())
lis=[]
for i in range(n):
    ele=int(input())
    lis.append(ele)
lis=sorted(lis)
print("smallest num is",lis[0])
print("greatest num is",lis[n-1])
