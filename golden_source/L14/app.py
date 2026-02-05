from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

# Route 1: Homepage
@app.route('/')
def home():
    return """
    <h1>Welcome to the L14 Golden Source App</h1>
    <p>Explore the routes:</p>
    <ul>
        <li><a href="/about">About</a></li>
        <li><a href="/user/GoldenUser">Dynamic User Route</a></li>
        <li><a href="/time">Current Time</a></li>
        <li><a href="/calc/add/10/5">Calculation (10 + 5)</a></li>
        <li><a href="/mult/5/5">Bonus: Multiplication Table (5x5)</a></li>
    </ul>
    """

# Route 2: About
@app.route('/about')
def about():
    return """
    <h1>About This App</h1>
    <p>This app demonstrates basic Flask routing concepts as part of Lesson 14.</p>
    <a href="/">Back Home</a>
    """

# Route 3: Dynamic Route
@app.route('/user/<name>')
def user_profile(name):
    try:
        # Simple error handling demonstration (though unlikely to fail here)
        clean_name = str(name).capitalize()
        return f"""
        <h1>Hello, {clean_name}!</h1>
        <p>This is a dynamic route that captures the name from the URL.</p>
        <a href="/">Back Home</a>
        """
    except Exception as e:
        return f"<h1>Error processing name: {e}</h1>"

# Route 4: Date/Time
@app.route('/time')
def current_time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <h1>Current Server Time</h1>
    <p>The time is: <strong>{now}</strong></p>
    <a href="/">Back Home</a>
    """

# Route 5: Logic/Calculation
@app.route('/calc/<op>/<int:a>/<int:b>')
def calculate(op, a, b):
    try:
        if op == 'add':
            result = a + b
            symbol = '+'
        elif op == 'sub':
            result = a - b
            symbol = '-'
        elif op == 'mul':
            result = a * b
            symbol = '*'
        elif op == 'div':
            if b == 0:
                return "<h1>Error: Cannot divide by zero</h1>"
            result = a / b
            symbol = '/'
        else:
            return f"<h1>Unknown operation: {op}</h1>"
        
        return f"""
        <h1>Calculation Result</h1>
        <p>{a} {symbol} {b} = <strong>{result}</strong></p>
        <a href="/">Back Home</a>
        """
    except Exception as e:
        return f"<h1>Error: {e}</h1>"

# Bonus: Multiplication Table
@app.route('/mult/<int:rows>/<int:cols>')
def multiplication_table(rows, cols):
    if rows > 20 or cols > 20:
        return "<h1>Too big! Keep it under 20x20.</h1>"
    
    html = "<h1>Multiplication Table</h1><table border='1' cellpadding='5'>"
    for r in range(1, rows + 1):
        html += "<tr>"
        for c in range(1, cols + 1):
            html += f"<td>{r * c}</td>"
        html += "</tr>"
    html += "</table><br><a href='/'>Back Home</a>"
    return html

if __name__ == '__main__':
    print("Starting L14 Flask App...")
    app.run(debug=True, port=5000)
