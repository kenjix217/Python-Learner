from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for contacts (resets on restart)
contacts = []

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Extract data from form
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Simple validation
    if name and email:
        new_contact = {
            'id': len(contacts) + 1,
            'name': name,
            'email': email,
            'message': message
        }
        contacts.append(new_contact)
        
    # Redirect to the contacts list
    return redirect(url_for('show_contacts'))

@app.route('/contacts')
def show_contacts():
    return render_template('contacts.html', contacts=contacts)

if __name__ == '__main__':
    print("Starting L15 Contact App...")
    app.run(debug=True, port=5001)
