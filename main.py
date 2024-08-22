# from functions import get_todos, write_todos
import time
import functions

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Enter add or show or edit or complete or exit: ")
    user_action = user_action.strip()
    user_action = user_action.lower()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)



    elif user_action.startswith("show"):
        todos = functions.get_todos()


        # Method for getting rid of excess space lines
        '''
        #new_todos = []

        
        for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item)
        '''
        # method2: new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}-{item}")

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("Error")
            continue

    elif user_action.startswith("exit"):
        break

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("Enter a todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    else:
        print("Hey, you entered an unknown command")

print("Bye!")




# how to edit strings since they are immutable
'''
filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames: #strings are immutable so we can't just change the index of the string we have to use a method filename is part of the list filenames but since we dealing with the individual strings in filenames we are dealing with strings
    filename = filename.replace('.', '-', 1) # the 1 is saying the first instance of . should be replaced with -
    print(filename)
'''


