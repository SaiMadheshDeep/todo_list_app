# Here i was import main source Todo.py file in package method
from Todo import Task
from termcolor import colored


# Create the object for Todo.py class object
obj=Task
print()
choice2=input("Wish you want continue (y/n) :")

# 1. Here i was use while loop because we don't know how many input to user input so i was use infinite Loop(while loop).
# 2. Here use not equal(!=) menthod in while loop , user enter the (N or n) the while loop is break otherwise any character to 
#    input user this while loop work infintly.

while choice2!="n" and choice2!="N":
       
       print(colored("Welcome To The Simple To-Do-List App !","cyan"))
       welcome=["1.Add Task","2.Complete Task","3.Show To-Do List","4.Save and quit"]
       for wel in welcome:
              print(wel)
              print(" ")
       print(colored("*...Choices only above interger values not a alphabet...*",'green'))
       try:
          choice=int(input("Enter Your Choice :"))
       except ValueError:
            print(colored("*...Choices are only integers not an alphabet...Try Again...*",'red'))
            
            print(' ')
            continue
       
       
       if choice==1:
            obj.task_add()
            print()
            choice2=input("Wish you want continue (y/n) :")
       elif choice==2:
            obj.task_Complete()
            print()
            choice2=input("Wish you want continue (y/n) :")
       elif choice==3:
            obj.display()
            print()
            choice2=input("Wish you want continue (y/n) :")
       elif choice==4:
            obj.save()
            print()
            choice2=input("Wish you want continue (y/n) :")
       else:
            obj.alart()
            print()
            choice2=input("Wish you want continue (y/n) :")
            
         