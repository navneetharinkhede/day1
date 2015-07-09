class Lnknode:
	def __init__(self,data,lnk=None):
		self.data=data
		self.lnk=lnk

class List:
	def __init__(self,front = None):
		self.front=front
	
	def insert(self,data):
		node = Lnknode(data)
		if(self.front==None):
			self.front = node
		else:
			n = self.front
			while n.lnk != None:
				n = n.lnk
			n.lnk=node
	def display(self):
			n=self.front
			while n != None:
				print n.data
				n=n.lnk

list=List()
list.insert(1)
list.insert(2)
list.insert(3)
list.insert(4)
list.display()
 
