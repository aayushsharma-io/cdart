# cdweb.py

from flask import Flask, request
from multiprocessing import Process

app = Flask(__name__)

@app.route('/')
def index():
    return 'CDWEB is ready!'

@app.route('/state', methods=['POST'])
def state():
    data = request.get_json()
    return data['message']

def run_server():
    app.run(debug=True)

if __name__ == '__main__':
    run_server()
