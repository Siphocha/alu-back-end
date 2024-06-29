"""Script exports data to CSV file."""
import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    #requesting user info by employee ID
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
    
    #convert json to dictionary
    user = json.loads(request_employee.text)
    username = user.get("username")
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))

    #dictionary to store tasks
    tasks = {}
    dictionary_organised_todos = json.loads(todos.text)

    #loop through dictionary & get completed tasks
    for dictionary in dictionary_organised_todos:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})

    #export dictionary organised data too CSV file
    with open('{}.csv'.format(argv[1]), mode='w') as file:
        file_editor = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for k, v in tasks.items():
            file_editor.writerow([argv[1], username, v, k])