#!/usr/bin/python3
"""
Exports the to-do list information for all employees to a JSON format.
"""
import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch all users and all todos simultaneously for efficiency
    users = requests.get(base_url + "users").json()
    todos = requests.get(base_url + "todos").json()

    # Map user IDs to usernames for quick lookup
    user_dict = {}
    for user in users:
        user_dict[user.get("id")] = user.get("username")

    # Initialize the main dictionary with empty lists for each user ID
    all_employees_data = {}
    for user_id in user_dict.keys():
        all_employees_data[user_id] = []

    # Populate the dictionary with tasks
    for task in todos:
        user_id = task.get("userId")
        task_info = {
            "username": user_dict.get(user_id),
            "task": task.get("title"),
            "completed": task.get("completed")
        }
        all_employees_data[user_id].append(task_info)

    # Write to JSON file
    with open("todo_all_employees.json", mode="w") as json_file:
        json.dump(all_employees_data, json_file)
