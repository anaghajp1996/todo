class ToDoList(object):
	

	def __init__(self):
		self.name=list_name
		self.to_do={}	#Basic Initialization of variables can be done this way
		self.done={}	

	#Implement the methods using Dictionaries instead of using Lists.	
	
	def add(self,task):
		self.to_do.append(task)

	def mark_done(self,done):
		
		self.done.append(done)
		self.to_do.remove(done)

	def see_tasks(self):
		print("To do list: ")
		for i in self.to_do:
			
			print(i)

		print("Done list: ")
		for j in self.done:
			print(j)



