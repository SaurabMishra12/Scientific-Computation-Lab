import numpy as np
import matplotlib.pyplot as plt

def steepest_descent(A, b, x0, max_iter, tol):
    
    x = x0.astype(float)
    path = [x.copy()]   #store iteration points
    
    print("Iteration 0 :", x)
    
    for k in range(1, max_iter + 1):
        
        #residual (negative gradient)
        r = b - A @ x
        
        #stopping condition
        if np.linalg.norm(r) < tol:
            print("Converged at iteration", k-1)
            break
        
        #optimal step length
        alpha = (r @ r) / (r @ A @ r)
        
        #update solution
        x = x + alpha * r
        
        path.append(x.copy())
        
        print(f"Iteration {k} :", x)
    
    return x, np.array(path)




A = np.array(eval(input("enter matrix A (e.g. [[3,1],[1,2]]): ")), dtype=float)
b = np.array(eval(input("enter vector b (e.g. [1,2]): ")), dtype=float)
x0 = np.array(eval(input("enter initial guess x0(format: [0,0]): ")), dtype=float)

max_iter = int(input("enter max iterations: "))
tol = float(input("enter the value for tolerance: "))


solution, points = steepest_descent(A, b, x0,max_iter,tol)

print("\napproximate solution:", solution)




plt.figure()
plt.plot(points[:,0],points[:,1],'o-',label ="iteration path")
true_sol= np.linalg.solve(A,b)
plt.scatter(true_sol[0],true_sol[1],marker ="*", s= 100, label ="True sol")
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("steepest descent iterations")
plt.legend()
plt.grid()
plt.show()
