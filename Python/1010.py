l=[]
for i in range(2):
    a, b, c = input().split()
    a=int(a)
    b=int(b)
    c=float(c)
    produto = b*c
    l+=[produto]

print("VALOR A PAGAR: R$ %.2f"% sum(l))
