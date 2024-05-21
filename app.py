# app.py

# GENERAL PSEUDO CODE
# define routes for rendering the form (/)
### handling form submission (/submit)
### and displaying the success message (/success) 

# use the redirect function to redirect user to success page after form submission

from flask import Flask, render_template, request, redirect, url_for

# Initialize Flask application
app = Flask(__name__)

# Route to render the HTML form for submitting user information
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Access form data submitted by the user
    name = request.form.get('name')
    email = request.form.get('email')
   
    # Print the submitted data to the console
    print(f"Received submission - Name: {name}, Email: {email}")
   
    # Redirect the user to the success page after form submission
    return redirect(url_for('success'))

# Route to render the success page after form submission
@app.route('/success')
def success():
    return render_template('success.html')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)