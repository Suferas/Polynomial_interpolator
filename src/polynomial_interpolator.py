import numpy as np
import sympy as sp
from sympy import *

sp.init_printing()


def operators(x, y):
    delta_y = []
    for a in range(len(x)):
        delta_y.append(y[a])

    for i in range(1, len(x)):

        for j in range(len(x)-1, i-1, -1):
            delta_y = [float(k) for k in delta_y]
            delta_y[j] = (delta_y[j]-delta_y[j-1])/(x[j]-x[j-i])
    return  delta_y

          

def polynomial_interpolator(set_of_x, set_of_y):
     set_of_x = [float(i) for i in set_of_x]
     set_of_y = [float(i) for i in set_of_y]
     set_of_operators = []
     set_of_operators = [float(i) for i in set_of_operators]
     set_of_operators.extend(operators(set_of_x, set_of_y)) 
     x = symbols('x') 
     
     def diferences_of_x(m):

          if m == 0:
               diference_of_x = 1
                         
          else:
               diference_of_x = x - set_of_x[m-1]

          return diference_of_x

     def recursive_diferences_of_x(q):

          set_of_diferences = []
          while q >= 0:
               if q == 0:
                    recursive_diference_of_x = 1
               else:
                    recursive_diference_of_x = diferences_of_x(q)*diferences_of_x(q-1)

               set_of_diferences.append(recursive_diference_of_x)
                    
               q-=2

          diferences = np.prod(set_of_diferences)

          return diferences

     def variable(i):
          variable = set_of_operators[i]*recursive_diferences_of_x(i)
          return variable

     set_of_variables = []
     for f in range(0, len(set_of_x), 2):

          if f == len(set_of_x)-1:
               recursive_variables = variable(f)
          
          else:
               recursive_variables = variable(f) + variable(f+1)

          
          set_of_variables.append(recursive_variables)

     
     sum_of_variables = sum(set_of_variables) 
     polynom = simplify(sum_of_variables, rational = True)

     return polynom
