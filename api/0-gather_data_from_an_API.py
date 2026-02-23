#!/usr/bin/python3
"""
Gathers data from a REST API for a given employee ID
and returns information about their TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    # Ensure an ID is passed as an argument
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data
    user_response = requests.get(base_url + "users/" + employee_id)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch todos data for the specific user
    todos_response = requests.get(base_url + "todos", params={"userId": employee_id})
    todos_data = todos_response.json()

    # Filter completed tasks and count totals
    completed_tasks = [task for task in todos_data if task.get("completed")]
    total_tasks = len(todos_data)

    # Print the first line
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), total_tasks))

    # Print each completed task with a tabulation and a space
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
