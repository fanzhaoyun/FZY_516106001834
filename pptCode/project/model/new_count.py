'''
from pub import add

print(add(4,5))
'''
'''
from model.pub import add

print(add(4,5))
'''
'''
from .count import A 

class B(A):
	def sub(self,a,b):
		return a - b 
		
result = B().add(2,5)
print(result)
'''
from count import A 

class B(A):
	def sub(self,a,b):
		return a - b 
		
result = B().add(2,5)
print(result)