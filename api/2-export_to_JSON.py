#!/usr/bin/python3
"""Export employee TODO list to JSON."""

import json
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

    task_list = []

    for task in todos:
        task_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        })

    json_data = {
        employee_id: task_list
    }

    with open("{}.json".format(employee_id), "w") as f:
        json.dump(json_data, f)
