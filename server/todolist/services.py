import requests

def get_todolist(port):
    url = 'http://127.0.0.1:' + port + '/api/Todo/'
    return requests.get(url)

def get_todo(port, todo_id):
    url = 'http://127.0.0.1:' + port + '/api/Todo/' + todo_id + '/'
    return requests.get(url)