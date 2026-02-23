#!/usr/bin/python3
"""
Exports an employee's to-do list information to a JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data to extract the username
    user_response = requests.get(base_url + "users/" + employee_id)
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch the to-do list for this specific user
    todos_response = requests.get(
            base_url + "todos", params={"userId": employee_id})
    todos_data = todos_response.json()

    # Build the required list of dictionaries
    task_list = []
    for task in todos_data:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        task_list.append(task_dict)
    # Wrap it in the main dictionary with the user ID as the key
    data_to_export = {employee_id: task_list}

    # Write the dictionary to a JSON file
    filename = "{}.json".format(employee_id)
    with open(filename, mode="w") as json_file:
        json.dump(data_to_export, json_file)
