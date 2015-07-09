epsilon = 0.000001
def square_root(a):
    if a==1:
       print a
    else:
       x=a-1
       while True:
          y = (x+a/x)/2
          if y==x:
             print y   
          else:     
             abs(x-y) <epsilon
             print y
             break 

