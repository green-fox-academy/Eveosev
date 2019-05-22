from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

#database
u_txt = open("user_info.txt", 'a+')
u_txt.write("username, password \n")
u_txt.close()

@app.route('/')
def signup_page():
    return render_template('signup.html')

@app.route('/submit_signup', methods = ["POST", "GET"])
def signup_info():
    if request.method == "POST":
        signup_infomation = request.form
        u_txt = open("user_info.txt", 'a+')
        u_database = u_txt.readlines()
        if f"{signup_infomation['uname']}"+", "+f"{signup_infomation['pin']}"+" \n" not in u_database:
                u_txt.write(f"{signup_infomation['uname']}, {signup_infomation['pin']} \n")
        else:
            return "The user has already existed"
    return f"{signup_infomation}"

# @app.route('/submit_login', methods = ["POST", "GET"])
# def login():
#     if request.method == "POST":
#         login_info = request.form
#         if login_info['uname'] in saved_info and 

@app.route('/welcome')
def welcome(username):
    return "welcome.html"


if __name__ == '__main__':
    app.run()

