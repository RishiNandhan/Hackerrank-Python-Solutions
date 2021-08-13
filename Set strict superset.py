s1=set(map(int,input().split()))
n=int(input())
a=[]
for i in range(n):
    s2=set(map(int,input().split()))
    a.append(s1.issuperset(s2))
if False in a:
    print(False)
else:
    print(True)



