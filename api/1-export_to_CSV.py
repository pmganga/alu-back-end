#!/usr/bin/python3
"""
Exports an employee's to-do list information to a CSV format.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user to get the username
    user = requests.get(base_url + "users/" + employee_id).json()
    username = user.get("username")

    # Fetch todos for the user
    todos = requests.get(base_url + "todos", params={"userId": employee_id}).json()

    # Create and write to the CSV file
    csv_filename = "{}.csv".format(employee_id)
    with open(csv_filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
