import mysql.connector
import prettytable

# Connect to MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Sourabh",
            database="tasks"
        )
        return connection
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return None

# execution a SQL query
def execute_query(query):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        return result
    return None

# greet the user
def greet():
    print("Hello! I'm your chatbot. How can I assist you today?")
    
# show table
def show(result):
    if result:
        table = prettytable.PrettyTable()
        table.field_names = ["ID", "Name", "Priority", "Due Date", "Status", "Info"]
        
        for row in result:
            table.add_row(row)
        
        print(table)
    else:
        print("Sorry, I couldn't fetch the data. Please check your database connection.")
        
# delete task
def delete_task(task_id):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            query = "DELETE FROM tasks WHERE sr_no = %s;"
            data = (task_id,)
            cursor.execute(query, data)
            connection.commit()
            connection.close()
            print("Task deleted successfully!")
    except mysql.connector.Error as err:
        print("Error: {}".format(err))

# Function to respond to user input
def respond(user_input):
    if "hello" in user_input.lower() or "hi" in user_input.lower():
        print("Hi there!")
    elif "how are you" in user_input.lower():
        print("I'm just a computer program, so I don't have feelings, but I'm here to help you!")
    elif "what is your name" in user_input.lower():
        print("My name is __Rohan__")
    elif "bye" in user_input.lower():
        print("Goodbye! Have a great day.")
        return True  # Exit the chatbot
    elif "add new task" in user_input.lower() or "new task" in user_input.lower():
        name=input("ok what is the task name\nYou: ")
        priority=input("set the priority for the task\nYou: ")
        duedate=input("fix a due date for your task (the format should be YYYY-MM-DD)\nYou: ")
        status=0
        info=input("want to add any additional info. ?(if not put a dot (.))\nYou: ")
        try:
            connection = connect_to_database()
            if connection:
                cursor = connection.cursor()
                query = "INSERT INTO tasks (name, priority, DueDate, status, info) VALUES (%s, %s, %s, %s, %s);"
                data = (name, priority, duedate, status, info)
                cursor.execute(query, data)
                connection.commit()
                connection.close()
                print("Task added successfully!")
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
        query = "INSERT INTO tasks (name, priority, DueDate, status, info) VALUES ('%s', %s, '%s', %s, '%s');"%(name, priority, duedate, status, info)
        result = execute_query(query)
    elif "show data" in user_input.lower() or "show tasks" in user_input.lower():
        query = "SELECT * FROM tasks.tasks;"
        result = execute_query(query)
        show(result)
    elif "delete task" in user_input.lower() or "delete a task" or "remove task" in user_input.lower() or "remove a task":
        task_id = input("Enter the task ID to delete: ")
        delete_task(task_id)
    else:
        print("I'm sorry, I don't understand that. Can you please ask another question or provide more details?")

# Main function to run the chatbot
def main():
    greet()
    while True:
        user_input = input("You: ")
        exit_chat = respond(user_input)
        if exit_chat:
            break

if __name__ == "__main__":
    main()