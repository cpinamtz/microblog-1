from app import instance


@instance.route('/')
@instance.route('/index')
def index():
    return "Hello, World!"
