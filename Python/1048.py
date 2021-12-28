def reajuste(n):
    if n >= 0 and n <= 400:
         r=0.15
    elif n >= 400.01 and n <= 800:
         r=0.12
    elif n >= 800.01 and n <= 1200:
         r=0.10
    elif n >=1200.01 and n <= 2000:
         r=0.07
    elif n > 2000:
         r=0.04
    ovo= "%0.2f"%(n*(1+r))
    Reajuste="%0.2f"%(n*(r))
    percentual = int(r*100)
    print("Novo salario: {}".format(ovo))
    print("Reajuste ganho: {}".format(Reajuste))
    print("Em percentual: {} %".format(percentual))
    
reajuste(float(input()))
