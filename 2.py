
def ack(m,n):
     if m==0:
	c=n+1
        return c
     elif m>0 and n==0 :
         c=ack(m-1,1)
         return c
     elif m>0 and n>0 :
         c=ack(m-1,ack(m,n-1))
         return c
print ack(3,4)

