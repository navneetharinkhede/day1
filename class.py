class Animal():
	def __init__(self,name,s):
		self.name = name
		self.talk = s
	
	def sound(self):
		print self.talk

animal1=Animal("dog","bark")
print animal1.sound()
		    
