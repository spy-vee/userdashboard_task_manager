# Step 1: Initialize an empty dictionary to store users
user_database = {}

# Step 2: Function to register a user
def register_user():
    print("\n--- Register ---")
    username = input("Enter a username: ")
    if username in user_database:
        print("Username already exists! Try again.")
        return
    password = input("Enter a password: ")
    if len(password) < 6:
        print("Password must be at least 6 characters long!")
        return
    user_database[username] = password
    print("Registration successful!")


# Step 3: Function to log in a user
def login_user():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    if username not in user_database:
        print("Username not found! Please register first.")
        return
    password = input("Enter your password: ")
    if user_database[username] == password:
        print(f"\nWelcome back, {username}!")
        user_dashboard(username)
    else:
        print("Incorrect password! Try again.")

# Step 4: Function to update a user profile
user_details = {}
def update_profile(username):
    print(f"\n--- Update Your Profile: {username} ---")
    name = input("Enter your given name: ")
    address = input("Enter your address: ")
    phone_number = input("Enter your phone number: ")
    date_of_birth = input("Enter your date of birth: ")
    user_details["name"] = name
    user_details["address"] = address
    user_details["phone_number"] = phone_number
    user_details["date_of_birth"] = date_of_birth
    print("\n--- Profile Updated ---")
    for key, value in user_details.items():
        print(f"{key}: {value}")

# Step 5: Task Dashboard
tasks = {}
# Function to add task for a user
def add_tasks():
    task_id = len(tasks) + 1   #usualy resolves to 1 or is 1
    task = input("Enter your task: ")
    tasks[task_id] = task
    print("\n--- Add Task Summary ---")
    print(f"Task added: {task}")

# Function to update a user's task
def update_tasks():
    update_id = int(input("Enter task id to update: "))
    if update_id in tasks:
        update_task = input("Update your task: ")
        tasks[update_id] = update_task
        print("\n--- Update Task Summary ---")
        print(f"Task updated: {update_task}")
    else:
        print("\n--- Error Task Summary ---")
        print(f"Task id {update_id} not found!")

# Function to delete tasks
def delete_tasks():
    remove_task = int(input("Enter the task id to delete task:"))
    if remove_task in tasks:
        deleted_task = tasks.pop(remove_task)
        print("\n--- Delete Task Summary ---")
        print(f"{deleted_task} was deleted!")
    else:
        print("\n--- Error Task Summary ---")
        print("Task id not found!")

# Function to view tasks
def view_tasks():
    if not tasks:
        print("\n--- Error Task Summary ---")
        print("No tasks assigned!")
        return

    print("\n--- View Task Summary ---")
    for key, value in tasks.items():
        print(f"{key}: {value}")

# Function to display task dashboard
def task_dashboard(username):
    while True:
        print(f"\n--- Task Dashboard: {username} ---")
        print("1. Add Task")
        print("2. View Task")
        print("3. Delete Task")
        print("4. Update Task")
        print("5. Exit")
        choice = input("Enter your choice (1, 2, 3 or 4): ")

        if choice == "1":
            add_tasks()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_tasks()
        elif choice == "4":
            update_tasks()
        elif choice == "5":
            user_dashboard(username)
            print(f"Goodbye, {username}!")
            break
        else:
            print("Invalid choice! Please try again.")

# Step 6: Dashboard after successful login
def user_dashboard(username):
    while True:
        print(f"\n--- Dashboard: {username} ---")
        print("1. Update Profile")
        print("2. View Profile")
        print("3. Task Dashboard")
        print("4. Change Password")
        print("5. Logout")
        choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if choice == "1":
            update_profile(username)
        elif choice == "2":
            view_profile(username)
        elif choice == "3":
            task_dashboard(username)
        elif choice == "4":
            change_password(username)
        elif choice == "5":
            print(f"Goodbye, {username}!")
            break
        else:
            print("Invalid choice! Please try again.")

# Step 7: View Profile
def view_profile(username):
    print(f"\n--- Profile ---")
    print(f"Username: {username}")
    print("Welcome to your dashboard!")


# Step 8: Change Password
def change_password(username):
    print("\n--- Change Password ---")
    old_password = input("Enter your current password: ")
    if user_database[username] != old_password:
        print("Incorrect current password! Password not changed.")
        return
    new_password = input("Enter a new password: ")
    if len(new_password) < 6:
        print("Password must be at least 6 characters long!")
        return
    user_database[username] = new_password
    print("Password updated successfully!")


# Step 9: Main program loop
while True:
    print("\n--- User Dashboard Management System ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
