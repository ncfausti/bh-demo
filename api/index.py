from flask import Flask, request
# import praw
# import os

app = Flask(__name__)
# reddit = praw.Reddit(
#     client_id=os.getenv('REDDIT_CLIENT_ID'),
#     client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
#     user_agent="MyGreatApp UA 1.2.4",
# )

@app.route("/api/hello")
def hello_world():
    print(request.path)
    return "<p>Hello, user!</p>"


@app.route("/api/data")
def get_data():
    return "<p>Hello, data!</p>"


@app.route('/api/greet/<string:name>')
def greet(name):
    return f"Hello, {name}!"


@app.route('/api/post_example', methods=['GET', 'POST'])
def post_example():
    print(request.path)
    return {'message': f'Received data: {request.path}'}
