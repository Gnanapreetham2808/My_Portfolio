import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY') or 'your-secret-key-here'  # Required for flash messages

# Configuration
SUBMISSIONS_FILE = "submissions.txt"

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()
        
        # Basic validation
        if not all([name, email, message]):
            flash('All fields are required!', 'error')
            return redirect(url_for('home'))
        
        # Write to file
        with open(SUBMISSIONS_FILE, "a") as f:
            f.write(f"{name} | {email} | {message}\n")
        
        flash('Thank you for your message!', 'success')
        return redirect(url_for('home'))
        
    except Exception as e:
        app.logger.error(f"Error processing submission: {str(e)}")
        flash('An error occurred. Please try again.', 'error')
        return redirect(url_for('home'))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=os.environ.get('DEBUG', 'False') == 'True')
