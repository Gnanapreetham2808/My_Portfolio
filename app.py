from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    with open("submissions.txt", "a") as f:
        f.write(f"{name} | {email} | {message}\n")
    return "Thank you for contacting!"

if __name__ == "__main__":
    app.run(debug=True)
