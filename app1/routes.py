from app1 import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World from App 1!"
