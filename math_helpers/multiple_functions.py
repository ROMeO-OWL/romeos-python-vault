def ContarDigPares(n): # multiple even 2%n==0
    cont = 0
    while n > 0:
        sem = n % 10
        if sem % 2 == 0:
            cont+=1
        n //=10
    return cont 

def ContarDigImpar(n): # multiple odd 2%n !=0
    cont = 0
    while n > 0:
        sem = n % 10
        if sem % 2 != 0:
            cont +=1
        n //=10
    return cont 

def ContarDigMult5(n): # multiple 5
    cont  = 0
    while n > 0:
        sem = n % 10
        if sem % 5 == 0:
            cont +=1
        n //=10
    return cont

def ContarDigMult6(n): # multiple 6
    cont = 0
    while n > 0:
        sem = n % 10
        if sem % 6 == 0:
            cont +=1
        n //=10
    return cont 
