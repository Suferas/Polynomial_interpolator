from polynomial_interpolator import operators, polynomial_interpolator
from sympy import *
import numpy as np
from matplotlib import pyplot as plt

set_of_x = []
set_of_y = []


number_of_elements = int(input("Number of elements: "))

for i in range(number_of_elements):
     if i == 0:
          elements_of_x = input('Set of x: \n')
          
          set_of_x.append(elements_of_x)
     else:
          elements_of_x = input()
          
          set_of_x.append(elements_of_x)
for i in range(number_of_elements):
     if i == 0:
          elements_of_y = input('Set of f(x):\n')
                    
          set_of_y.append(elements_of_y)

     else:
          elements_of_y = input()
          set_of_y.append(elements_of_y)


y = polynomial_interpolator(set_of_x, set_of_y)
print('\nPolynomial:\n '+str(y))


x = symbols('x')
f_x = lambdify(x, y, modules=['numpy'])

x_values = np.linspace(int(min(set_of_x))-100, int(max(set_of_x))+100, 500)
y_values = f_x(x_values)

fig, ax = plt.subplots()

ax.plot(x_values, y_values, label = 'y = '+str(y))
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

plt.title('Function graph')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(alpha=.4, linestyle = '-')
plt.legend(prop = {'size':6})
plt.show()
