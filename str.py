def print_n(s,n):
    if n<=0:
       return
    else:  
       print s
       print_n(s,n-1)
       return 
print_n('ajith',5)
