import numpy as np
from numpy.linalg import eigh, norm

A = np.array([[-5, 2, 3],
 	     [2, 5, 1],
 	     [-3, 1, -5]])
 	     
ev, V =eigh(A.T@A)

u0 =A@V[:,0]/norm(A@V[:,0])  #normalizing 
u1 =A@V[:,1]/norm(A@V[:,1])
u2 =A@V[:,2]/norm(A@V[:,2])

U =np.array([u0,u1,u2]).T
U_afterSVD = np.round(U.T@A@V,decimals =5) #diagonal matrix
print("Matrix after rounding: \n",U_afterSVD)
print("\nMatrix before rounding: \n",U)
