from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    print("during home view")
    return "home view"


@app.route("/fuck-you")
def fuck():
    print("during fuck view")
    return "fuck view"


@app.before_request
def show_before():
    print("before request")


@app.teardown_request
def show_teardown(exception):
    print("after request")


with app.test_request_context():
    print("during with block")

# teardown functions are called after the context with block exits

with app.test_client() as client:
    client.get("/")
    # the contexts are not popped even though the request ended
    print(f"========= path url {request.path} =========")

with app.test_client() as client:
    client.get("/fuck-you")
    # the contexts are not popped even though the request ended
    print(f"========= path url {request.path} =========")

app.run()

# the contexts are popped and teardown functions are called after
# the client with block exits
