n=int(input())
l=[]
q=[]
for i in range(n):
    t=(input().split())
    
    l.append(t)
d=dict(l)
print(d)
for j in range(n):
    q.append(input())

for k in q:
    if k in d:
        print("{}={}".format(k,d[k]))
    else:
        print("Not found")
