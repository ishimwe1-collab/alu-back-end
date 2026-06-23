#!/usr/bin/python3

"""Export employee TODO list to JSON."""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    ).json()

    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params={"userId": employee_id}
    ).json()

    tasks = []

    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        })

    data = {
        employee_id: tasks
    }

    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump(data, json_file)
