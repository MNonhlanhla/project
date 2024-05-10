from datetime import date
import sys

# Prompt the user for the login credentials.
username = input("Enter your username: ")
password = input("Enter your password: ")

# Initialize the user_logged_in flag which will be changed when the credentials are valid.
user_logged_in = False


''' This function registers a new user and saves the username and password
 in user.txt file after the credentials have been confirmed. '''
def user_reg():
    new_username = input("Enter your new username: ")
    new_password = input("Enter your new password: ")
    password_confirmation = input("Enter the same password again for confirmation: ")
    if new_password == password_confirmation:
        with open("user.txt", "a") as user_file:
            user_file.writelines(f"\n{new_username},{new_password}")
    else:
        print("The passwords your entered do not match")


'''This function prompts the user for their username and the task details.
Opens a tasks.txt file and adds the task in the file.'''
def add_task():
    task_username = input("Enter your username ")
    title = input("Enter the title of the task ")
    task_description = input("Enter the description of the task ")
    task_due_date = input("Enter the task due date (dd MMM yyyy, ie 01 Jan 2000) ")
    current_date = date.today()
    with open('tasks.txt', 'a') as tasks:
        tasks.write(f'''{task_username}, {title}, {task_description}, {task_due_date}, {current_date}, No\n''')
    print("Task added successfully")


'''This function opens tasks.txt file for reading and prints out all the tasks from the file.'''


def view_all():
    with open('tasks.txt', 'r') as tasks:
        task_list = tasks.readlines()
        for task in task_list:
            task_elements = task.split(",")
            print(f"Task: \t{task_elements[1]}")
            print(f"Assigned to: \t{task_elements[0]}")
            print(f"Date assigned: \t{task_elements[3]}")
            print(f"Due date: \t{task_elements[4]}")
            print(f"Task completed: \t{task_elements[5]}")
            print(f"Task description: \n{task_elements[2]}")
            print("\n")


'''This function opens tasks.txt file, reads data to check for the tasks that only belongs to the logged in user
Prints all the tasks and allow the user to ether edit r mark the task as done.'''
def view_mine():
    with open('tasks.txt', 'r') as tasks:
        task_list = tasks.readlines()
        task_count = 0
        for task in task_list:
            task_elements = task.split(",")
            user = task_elements[0]
            if user == username:
                print(task_count)
                print(f"Task: \t{task_elements[1]}")
                print(f"Assigned to: \t{task_elements[0]}")
                print(f"Date assigned: \t{task_elements[3]}")
                print(f"Due date: \t{task_elements[4]}")
                print(f"Task completed: \t{task_elements[5]}")
                print(f"Task description: \n{task_elements[2]}")
                print("\n")
            task_count += 1

        task_number = int(input('''Please select the task you want to view by entering a task number or 
        -1 if you want to go back to the main menu: '''))
        selected_task = task_list[task_number]
        action = input("Please enter edit to edit the task or mark to mark the task as complete: ")

        if action.lower() == "mark":
            with open('tasks.txt', 'a') as file:
                task_list = selected_task.split(",")
                task_list[5] = "Yes"
                task = ','.join(task_list)
                file.writelines(task)

        elif action.lower() == "edit":
            print("You can only edit the username and the due date of the incomplete task")
            edit_action = input("What would you like to edit: username or date: ")
            if edit_action.lower() == "username":
                new_username = input("Enter your new username: ")
                with open('tasks.txt', 'a') as file:
                    task_elements = selected_task.split(",")
                    task_elements[0] = new_username
                    task = ','.join(task_elements)
                    file.writelines(task)

            elif edit_action.lower() == "date":
                new_due_date = input("Enter new desired due date: ")
                with open('tasks.txt', 'a') as file:
                    task_elements = selected_task.split(",")
                    task_elements[4] = new_due_date
                    task = ','.join(task_elements)
                    file.writelines(task)


''' Opens user.txt file for reading the user credentials when they trying to log in. '''
with open("user.txt", "r") as task_file:
    lines = task_file.readlines()
    count = 0
    while not user_logged_in:
        for index in range(0, len(lines)):
            credentials = lines[index]
            username_password_list = credentials.split(',')
            registered_username = username_password_list[0]
            registered_password = username_password_list[1].strip()

            # Check if the credentials are valid and mark the user as logged in.
            if registered_username == username and registered_password == password:
                print("Welcome " + registered_username)
                user_logged_in = True
                continue
        if user_logged_in:
            continue
        elif count < 2:
            print("Wrong username or password")
            username = input("Please enter your username ")
            password = input("Please enter your password ")
            count += 1
        else:
            # The user at this point would have entered their credentials 3 times.
            print("Please try again.")
            break

''' When the user is successfully logged in, they are presented with menu options. '''
if user_logged_in:
    while True:
        menu = ""
        if username.lower() == "admin":
            menu = input('''Select one of the following options:
        r - register a user
        a - add task
        va - view all tasks
        vm - view my tasks
        gr - generate reports
        ds - display statistics
        e - exit
        : ''').lower()
        # Present the menu to the user and 
        # make sure that the user input is converted to lower case.
        else:
            menu = input('''Select one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
    : ''').lower()

        if menu == 'r':
            user_reg()
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all()
        elif menu == 'ds':
            with open('tasks.txt', 'r') as task_file:
                lines = task_file.readlines()
                print(f"The total number of users is {len(lines)}\n")
                print(f"And the total number of tasks is {len(lines)}\n")
        elif menu == 'vm':
            view_mine()
        elif menu == 'e':
            print('Goodbye!!!')
            sys.exit()
        else:
            print("You have entered an invalid input. Please try again")
            
