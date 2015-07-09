def square_root(a):
   if a==1:
      x=1
   else:
      x=a-1
      while True:
            y = (x+a/x)/2
            if y==x:
               print y
               break
               x = y
 
def test_sqre_root():
    import math
    i=1
    while i<= 10:
          c = square_root(i)
          d = math.sqrt(i)
          print float(i),
          print	float(c),
          print float(d)
          i=i+1 
test_sqre_root()

