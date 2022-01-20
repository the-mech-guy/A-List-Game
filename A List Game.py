x = int(input())
t = 2
k=0

while x>=t*t:
    if(x%t == 0):
        x/=t
        k+=1
    else:
        t+=1

print(k+1)