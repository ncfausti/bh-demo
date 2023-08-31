from flask import Flask, request
# import praw
# import os

app = Flask(__name__)
# reddit = praw.Reddit(
#     client_id=os.getenv('REDDIT_CLIENT_ID'),
#     client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
#     user_agent="MyGreatApp UA 1.2.4",
# )
initial_data = [
    { "name": 1, "cost": 4.11, "impression": 100 },
    { "name": 2, "cost": 2.39, "impression": 120 },
    { "name": 3, "cost": 1.37, "impression": 150 },
    { "name": 4, "cost": 1.16, "impression": 180 },
    { "name": 5, "cost": 2.29, "impression": 200 },
    { "name": 6, "cost": 3, "impression": 499 },
    { "name": 7, "cost": 0.53, "impression": 50 },
    { "name": 8, "cost": 2.52, "impression": 100 },
    { "name": 9, "cost": 1.79, "impression": 200 },
    { "name": 10, "cost": 2.94, "impression": 222 },
    { "name": 11, "cost": 4.3, "impression": 210 },
    { "name": 12, "cost": 4.41, "impression": 300 },
    { "name": 13, "cost": 2.1, "impression": 50 },
    { "name": 14, "cost": 8, "impression": 190 },
    { "name": 15, "cost": 0, "impression": 300 },
    { "name": 16, "cost": 9, "impression": 400 },
    { "name": 17, "cost": 3, "impression": 200 },
    { "name": 18, "cost": 2, "impression": 50 },
    { "name": 19, "cost": 3, "impression": 100 },
    { "name": 20, "cost": 7, "impression": 100 },
    { "name": 21, "cost": 4.3, "impression": 210 },
    { "name": 22, "cost": 4.41, "impression": 300 },
    { "name": 23, "cost": 2.1, "impression": 50 },
    { "name": 24, "cost": 8, "impression": 190 },
    { "name": 25, "cost": 0, "impression": 300 },
    { "name": 26, "cost": 9, "impression": 400 },
    { "name": 27, "cost": 3, "impression": 200 },
    { "name": 28, "cost": 2, "impression": 50 },
    { "name": 29, "cost": 3, "impression": 100 },
    { "name": 30, "cost": 7, "impression": 100 },
    { "name": 31, "cost": 2, "impression": 50 },
    ]

@app.route("/api/hello")
def hello_world():
    print(request.path)
    return "<p>Hello, user!</p>"


@app.route("/api/data")
def get_data():
    return f"<p>Hello</p><code>{initial_data}</code>"


@app.route('/api/greet/<string:name>')
def greet(name):
    return f"Hello, {name}!"


@app.route('/api/post_example', methods=['GET', 'POST'])
def post_example():
    print(request.path)
    return {'message': f'Received data: {request.path}'}
