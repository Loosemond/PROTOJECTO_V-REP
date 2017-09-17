# -*- coding: utf-8 -*-
"""
Laboratórios de Matemática
Created on Fri May 12 15:12:16 2017
@author: Antonio
"""
from __future__ import division
from __future__ import print_function
from LabMat1_Lib import *
import pylab as pl

clc()

#%

#%% RESOLUÇÃO Simbólica

#%% solução geral
x=sym('x')				# definir x como v. ind.
y=Function('y')  			# definir y como v. dep.
C=symbols('C{}'.format(1))  	# definir a constante C1
EDO=Eq(Diff(y(x),x),-x*y(x)/2)	# definir a EDO
display(EDO)
sol=dsolve(EDO,y(x))		# obter a solução geral
display(expand(sol))

#%% solução particular
x0=-2; y0=1
C1=solve(subs(subs(sol,x,x0),y(x0),y0),C)[0]
sp=subs(sol,C,C1)
display(sp)
figure(1); ezplot(sp.rhs,[-4,4])
axis([-4,4,-3,3]);grid(1)

#%% Campos de direções
m=double(subs(subs(EDO.rhs,x,x0),y(x0),y0))
rt=y0+m*(x-x0);
rtt=ezplot(rt,[-4,4])
setp(rtt,c='g',ls=':')
arrow(x0,y0,1,m,color='r',width=0.005)
show()

#%% Campo de direcções numa malha
X=linspace(-4,4,9)
Y=linspace(-3,3,7)
figure(2)
for x0 in X:
    for y0 in Y:
        m=double(subs(subs(EDO.rhs,x,x0),y(x0),y0))
        Norma=2*pl.sqrt(1+m**2);
        arrow(x0,y0,1/Norma,m/Norma,color='r',width=0.005)
axis([-4,4,-3,3]);grid(1)
show()

#%%
x=sym('x')
y=sym('y')
f=inline(x+exp(-y),(x,y))

# comando com os parâmetros adicionais por defeito
CampoVetores(f(x,y),(x,y));show() 
# e com os parâmetros adicionais escolhidos
CampoVetores(f(x,y),(x,y),J=[-3,4,-3,3],d=[2,2],norm=False)

# idem para linhas de campo
LinhasCorrente(f(x,y),(x,y),J=[-3,4,-3,3],d=[2,2]); show()

#%%
#%% Método de Euler
#%% aplicar ao PVI: y'=x+exp(-y); CI y(-4)=-4;
x,y=sym('x y')  # ATENÇÃO: x e y são variáveis simbólicas!
f=inline(x+exp(-y),(x,y)) 	# definir f(x,y) da EDO y'=f(x,y)
Jnl=[-5,5,-4,4]; 

# aplicar o método de Euler com os parâmetros por defeito
xx0,yy0=Euler(f(x,y),(x,y)); # x0=0; y0=0; xf=5; h=0.1

# alterar os parâmetros adicionais
xx,yy=Euler(f(x,y),(x,y),x0=-4,y0=-4,xf=4,h=0.01);

# representar as soluções
plot(xx0,yy0,'.r',xx,yy, '-b'); grid('on')

# sobrepor as linhas de corrente
LinhasCorrente(f(x,y),(x,y),J=Jnl)
show()

#####################################################################
#####################################################################
#disp('Exercicios de consolidação')###################################
#####################################################################
#####################################################################
disp('Exercicio 1')
#A taxa de desintegração de uma dada substância radioactiva é proporcional à sua massa nesse instante.
disp('a)')
t=sym('t')
k=sym('k') #constante de decaimento radioativo
M=Function('M')
C=symbols('C{}'.format(1)) 
EDO = Eq(Diff(M(t),t),-k*M(t)) # definir a EDO
display(EDO)
sol=dsolve(EDO,M(t))		# obter a solução geral
display(expand(sol))

disp('b)')
t0=sym('t0')
M0=sym('M0')

C1=solve(subs(subs(sol,t,t0),M(t0),M0),C)[0]
sp=subs(sol,C,C1)
sp=simplify(sp)
display(sp)

disp('c)')
ta=5730
Ma=M0/2
eq=Eq(subs(sp.lhs,M(t),Ma),subs(subs(sp.rhs,t,ta),t0,0))
display(eq)
from sympy import solve
#k1 = solve((eq.lhs-eq.rhs)/M0,k)
k1 = solve(Eq(ln(1/2),-k*5730),k)[0]
print (k1)

#0.05*M0=M0*exp(-k1*(t-t0))
#t=24778 anos.

disp('Exercicio 2')
t=sym('t')
v=Function('v')
C=symbols('C{}'.format(1)) 
F=25E3
m=1E3
EDO = Eq(m*Diff(v(t),t)+900*v(t),F)
display(EDO)
sol=dsolve(EDO,v(t))		# obter a solução geral
display(expand(sol))
C1=solve(subs(subs(sol,t,0),v(0),0),C)[0]
velocidade=subs(sol,C,C1)
display(velocidade)

ezplot(velocidade.rhs,[0,20])
show()

#velocidade maxima 
#dvelocidade = diff(velocidade.rhs,t)  #por aqui não dá pq não há zero da derivada.
#t_=solve(dvelocidade,t)[0]
#vmax=subs(velocidade,t,t_)
#display(vmax)

eq1=Eq(F-900*v(t),0)
display(eq1)
s=solve(eq1,v(t))[0]  #velocidade limite quando a aceleração é zero!!!
display(s)

disp('Exercicio 3')

x=sym('x')
y=Function('y')
C=symbols('C{}'.format(1))  
#EDO=Eq(Diff(y(x),x)+y(x)*cos(x),sin(2*x))#Preciso de abrir o sin(2*x)
EDO=Eq(Diff(y(x),x)+y(x)*cos(x),2*sin(x)*cos(x))
sol=dsolve(EDO,y(x))
x0=-5
y0= 1
C1=solve(y0-subs(subs(sol.rhs,x,x0),y(x),y0),C)[0]
sp=subs(sol,C,C1)

figure()
ezplot(sp.rhs,[-5,5])

#Euler
x,y=sym('x y')
f=inline(2*sin(x)*cos(x)-y*cos(x),(x,y))
xx1,yy1=Euler(f(x,y),(x,y),x0=-5,y0=1,xf=5,h=0.1);

plot(xx1,yy1,'-r')
show()

disp('Exercicio 4')
L=1
R=5
t,i=sym('t i')
v=inline(Piecewise((0,t<0),(5,t<=4),(5*cos(pi*t),t>4)),t)
i0=0

f=inline(v(t)/L-R*i/L,(t,i)) 	# definir f(x,y) da EDO y'=f(x,y)
Jnl=[0,15,-3,3]; 

## alterar os parâmetros adicionais
tt,ii=Euler(f(x,y),(x,y),x0=0,y0=0,xf=15,h=0.1);

# representar as soluções
plot(tt,ii, '-b'); grid('on')

## sobrepor as linhas de corrente
LinhasCorrente(f(x,y),(x,y),J=Jnl)
show()

CampoVetores(f(x,y),(x,y),J=Jnl,d=[1,1],norm=False)
show()




