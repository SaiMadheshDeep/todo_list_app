from termcolor import colored
import re
# This empty list use for store the user input task.
lis_task=[]

class Task:    
        
        # This function use for user input task to adding task.    
        def task_add():
                
                pend=" -Pending"
                add=input("Enter Your Task :") + pend + "\n"
                print("Task Added Successfully !")
                lis_task.append(add)
                file = open('todo_list.txt','a')
                file.write(add)
                
     
        # This function use for user input complete task to work base in index value to mark as complete task in list.
        def task_Complete():
              
                # define the filename and the line number to delete
                # define the filename and the line number to remove
        
                filename = "todo_list.txt"
                print(" ")
                file=open('todo_list.txt','r')
                print(file.read())
                line_number_to_remove = int(input("Enter the task number to mark as completed :"))
                print('Task mark as completed')
         
               #delt=(line_number_to_remove - 1)

                # open the file in read mode ('r')
                with open(filename, 'r') as file:
                # read all the lines into a list
                        lines = file.readlines()

                # open the file in write mode ('w'), this will overwrite the existing file
                with open(filename, 'w') as file:
                # write all the lines back to the file, skipping the line we want to remove
                         for i, line in enumerate(lines):
                                 if i+1!= line_number_to_remove:
                                         file.write(line)
                                         
        # 1.This function use for display a user input task list.
        # 2.And here i use enumerate method to use display a task list perfix add numbers order so, i was use enumerate method.
        
        def display():
                print(" ")
                print(colored("Your Task","light_yellow"))
                print(" ")
                file=open('todo_list.txt','r')
                print(file.read())
        # This function use for file handling , users enter the task's to store the text file("todo_list.txt").
       
        def save():
             
             print("Task's are successfully saved...!")
        # This function use for some times users enter the out of range of choice number so this function alart to users.
        
        def alart():
                
                 print(colored("!!...YOU WAS ENTER INVALID CHOICE NUMBER SO, KINDLY CHECK BELOW THE CHOICE NUMBERS & ENTER THE VALID CHOICE NUMBER...!!",'red'))
                 print()
                 welcome=["1.Add Task","2.Complete Task","3.Show To-Do List","4.Save and quit"]
                 for wel in welcome:
                    print(wel)
                    print(" ")
                
       
        
            
    
       
       
       
    
