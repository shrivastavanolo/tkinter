def sumn(n):
    if n==0:
        return 0
    else:    
        return sumn(n-1)+n   
print(sumn(5)) 

def factt(n):
    if n==0 or n==1:
        return 1
    else:
        return factt(n-1)*n
print(factt(5))

def powerr(a,b):
    if b==0:
        return 1
    else:
        return powerr(a,b-1)*a
print(powerr(2,5))





