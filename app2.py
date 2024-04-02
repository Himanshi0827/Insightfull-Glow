import csv
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Load existing users from CSV file
users = {}

def load_users():
    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            username, password = row
            users[username] = password

load_users()

def save_user_to_csv(username, password):
    with open('users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

@app.route('/')
def welcome_page():
    return render_template('welcome_page.html')

@app.route('/dots')
def dots():
    return render_template('9_dots.html')

@app.route('/home1')
def home_page():
    return render_template('home1.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/signup')
def signup_page():
    return render_template('signup.html')

@app.route('/contact')
def contact_us():
    return render_template('contact.html')

@app.route('/about')
def about_us():
    return render_template('about.html')

@app.route('/skin')
def skin():
    return render_template('skin_ass_form.html')
@app.route('/hair')
def hair():
    return render_template('hair_ass_form.html')

@app.route('/form/login', methods=['POST'])
def process_login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users and users[username] == password:
        return render_template('9_dots.html')
    else:
        return "Authentication Failed. Access denied."

@app.route('/form/signup', methods=['POST'])
def process_signup():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users:
        return "Username already exists. Try a different one."

    save_user_to_csv(username, password)
    return render_template('9_dots.html')


if __name__ == "__main__":
    app.run(debug=True)