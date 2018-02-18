class ToDoList(object):
	

	def __init__(self,list_name,to_do,done):
		self.name=list_name
		self.to_do=to_do
		self.done=done

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



