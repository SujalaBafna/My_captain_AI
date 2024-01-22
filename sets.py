import numpy as np
e= {8,0,6,2,4}
n= {1,3,5,2,4}
a= e|n
print ('the union of the two sets is: '+str(a))
b= e&n
print ("the intersection of the two sets is: "+str(b))
c= e-n
print ("the difference of the two sets is: "+str(c))
d= e^n
print ("the symmetric difference of the two sets is: "+str(d))
