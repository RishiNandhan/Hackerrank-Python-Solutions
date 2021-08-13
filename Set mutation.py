n=int(input())
s1=set(map(int,input().split()))
m=int(input())
for i in range(m):
    c,k=input().split()
    s2=set(map(int,input().split()))
    if c=="intersection_update":

        s1.intersection_update(s2)
    elif c=="update":

        s1.update(s2)
    elif c=="symmetric_difference_update":

        s1.symmetric_difference_update(s2)
    else:

        s1.difference_update(s2)

print(sum(s1))




