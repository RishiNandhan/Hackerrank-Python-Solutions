n=int(input())
for i in range(n):
    t1=int(input())
    s1=set(map(int,input().split()))
    t2=int(input())
    s2=set(map(int,input().split()))
    print(s1.issubset(s2))
