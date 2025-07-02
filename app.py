from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    with open("submissions.txt", "a") as f:
        f.write(f"{datetime.now()} | Name: {name}, Email: {email}, Message: {message}\n")

    return "<h2>Thanks for your message!</h2><a href='/'>Back to site</a>"

if __name__ == "__main__":
    app.run(debug=True)
