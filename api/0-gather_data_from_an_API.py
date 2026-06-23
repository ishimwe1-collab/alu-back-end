#!/usr/bin/python3
"""Fetch and display an employee's TODO list progress."""

import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    ).json()

    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params={"userId": employee_id}
    ).json()

    completed_tasks = [task for task in todos if task.get("completed")]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user.get("name"),
            len(completed_tasks),
            len(todos)
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
