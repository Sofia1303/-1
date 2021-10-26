from math import fabs

def task1(x):                              
	print('Задание 1\ninput',x)
	a=[]
	while x>0:
		a.append(x%10)
		x=x//10
	for i in range(int(len(a)/2)):
		if a[i] != a[len(a)-1-i]:
			return False
	return True

print('output',task1(11411),'\n')

def task2(x):                             
	print('Задание 2\ninput',x)
	l=[]
	a=[]
	b=[]
	c=[]
	for i in range (len(x)):
		if x[i]%2 == 0:
			a.append(x[i])
		if x[i]%3 == 0:
			b.append(x[i])
		if x[i]%5 == 0:
			c.append(x[i])
	l.append(a), l.append(b), l.append(c)
	print('output',l,'\n')
	return l

a1=task2([1,2,3,4,5,6,7,8,9,10])

def task3(x):
	print('Задание 3\ninput',x)
	l=[]
	sign=1
	if x<0:
		sign=-1
		x*=sign
	for i in range(len(str(x))):
		l.append(str(x)[i])
	x=0
	for i in range(len(l)):
		x+=int(l[i])*10**i*sign
	print('output',x,'\n')
	return x

a2=task3(-123)

def task4(A,n):
	print('Задание 4\ninput\nчисло',A,'\nстепень корня ',n)
	x=5;
	for i in range(100):
		if fabs(x-((n-1)*x+A/x**(n-1))/n)>0.0001:
			x=((n-1)*x+A/x**(n-1))/n
		else:
			break
	print('output\nкорень ',x,'\n')
	return x

a2=task4(2,7)

def task5(x):
	print('Задание 5\ninput',x)
	for i in range(2,int(x/2)):
		if x%i == 0:
			return False
	return True

print('output',task5(1234))

def decorator(funct, j=6):
	arg=0
	iter=0
	def hash(x):
		nonlocal arg
		nonlocal iter
		if iter == 0:
			arg=funct(x)
			iter=j
		else:
			arg=funct(arg)
			iter-=1
	return hash

@decorator
def plus(x):
	print(x+1)
	return x+1

print('\nЗадание7')

for i in range(10):
	plus(1)
