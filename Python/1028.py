n=int(input())
for i in range(n):
    a,b=input().split()
    a,b=int(a),int(b)
    while a%b!=0:
        resto=a%b
        a=b
        b=resto
    print(b)
