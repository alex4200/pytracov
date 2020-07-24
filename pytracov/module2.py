
def ackermann(m, n):
    """computes the value of the Ackermann function for the input integers m and n.
       the Ackermann function being:
       A(m,n)=n+1               if m=0
             =A(m-1,1)          if m>0 and n=1
             =A(m-1,A(m,n-1)    if m>0 and n>0"""
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ackermann(m-1,1)
    elif m>0 and n>0:
        return ackermann(m-1,ackermann(m,n-1)) 
