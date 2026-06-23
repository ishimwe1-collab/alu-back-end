#!/usr/bin/python3

"""Fetch and display an employee's TODO list progress."""

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    user = requests.get(
        "http://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    ).json()

    todos = requests.get(
        "http://jsonplaceholder.typicode.com/todos",
        params={"userId": employee_id}
    ).json()

    completed_tasks = []

    for task in todos:
        if task.get("completed") is True:
            completed_tasks.append(task)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user.get("name"),
            len(completed_tasks),
            len(todos)
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
