from flask import Flask # Importing flask class

app = Flask(__name__) # Creating instance of Flask Class
# __name__ : special variable signifying name of module
# if script ran directly, __name__ == __main__

@app.route("/")
def hello_world():

    return "<h5>Hello, World!</h5>"


# Need to set environment variable to the file that we want to be our flask application
# set FLASK_APP = flaskblog.py in cmd prompt

if __name__ == "__main__":
    app.run(debug = True, use_debugger = True)