#!/usr/bin/python3
"""Export employee TODO list to JSON."""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
<<<<<<< HEAD

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
            "task": task["title"],
            "completed": task["completed"],
            "username": user["username"]
        })

    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump({employee_id: tasks}, json_file)
=======

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
>>>>>>> 2b94313d19b5347d21b86848fdd40ffea50370c7
