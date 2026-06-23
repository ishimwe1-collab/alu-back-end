#!/usr/bin/python3
<<<<<<< HEAD
"""Gather data from an API."""
=======

"""Fetch and display an employee's TODO list progress."""
>>>>>>> 2b94313d19b5347d21b86848fdd40ffea50370c7

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
<<<<<<< HEAD

    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    ).json()

    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id
        )
    ).json()

    done_tasks = [task for task in todos if task.get("completed")]
=======

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
>>>>>>> 2b94313d19b5347d21b86848fdd40ffea50370c7

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user.get("name"),
<<<<<<< HEAD
            len(done_tasks),
=======
            len(completed_tasks),
>>>>>>> 2b94313d19b5347d21b86848fdd40ffea50370c7
            len(todos)
        )
    )

<<<<<<< HEAD
    for task in done_tasks:
=======
    for task in completed_tasks:
>>>>>>> 2b94313d19b5347d21b86848fdd40ffea50370c7
        print("\t {}".format(task.get("title")))
