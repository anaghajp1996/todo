from todo import ToDoList
list1=[]
done1=[]
mylist=ToDoList("New",list1,done1)

while True:

	option= int(input("Enter your option \n\
		1.Add new task\n\
		2.Mark task done\n\
		3.View list: "))

	if option==1:
		taskname=input("Enter name of task: ")
		mylist.add(taskname)

	elif option==2:
		print("YOUR LIST: ")
		
		for i,key in enumerate(list1):
			print(i+1,key)
			

		donenum=int(input("Enter task number to be marked as done: "))

		mylist.mark_done(list1[donenum-1])



	elif option==3:
		print("YOUR LIST: ")
		mylist.see_tasks()


	else:
		break
