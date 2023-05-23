# Solving simultaneous equations using Cramer's rule and Rule of Sarrus

import numpy as np

a = int(input('Number a = '))
b = int(input('Number b = '))
c = int(input('Number c = '))
d = int(input('Number d = '))
e = int(input('Number e = '))
f = int(input('Number f = '))
g = int(input('Number g = '))
h = int(input('Number h = '))
i = int(input('Number i = '))
j = int(input('Number j = '))
k = int(input('Number k = '))
l = int(input('Number l = '))


matrix1 = np.array([[a,b,c], [d,e,f], [g,h,i]])

print('Coefficient of unknown: ', matrix1)

matrix2 = np.array([[j,k,l]])

print('Constants: ', matrix2)


W = (a*e*i+b*f*g+c*d*h)-(c*e*g+a*f*h+b*d*i); print('It is W ', W)

Wx = (j*e*i+b*f*l+c*k*h)-(c*e*l+j*f*h+b*k*i); print('It is Wx ', Wx)

Wy = (a*k*i+j*f*g+c*d*l)-(c*k*g+a*f*l+i*d*j); print('It is Wy ', Wy)

Wz = (a*e*l+b*k*g+j*d*h)-(j*e*g+a*k*h+b*d*l); print('It is Wz ', Wz)


x = Wx/W; print('To jest x ', x)

y = Wy/W; print ('To jest y ', y)

z = Wz/W; print ('To jest z ', z)