main.py
from flask import Flask, render_template, request

app = Flask(__name__)

def result_calculate(size, lights, device):
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<size>')
def lights(size):
    return render_template('lights.html', size=size)

@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template('electronics.html', size=size, lights=lights)

@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    result = result_calculate(int(size), int(lights), int(device))
    return render_template('end.html', result=result)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']  
    date = request.form['date']


    with open('form.txt', 'a') as f:
        f.write(f"Name: {name}\n")
        f.write(f"Email: {email}\n")
        f.write(f"Address: {address}\n")
        f.write(f"Date: {date}\n\n")

    return render_template('form_result.html', name=name, email=email, address=address, date=date)

if __name__ == '__main__':
    app.run(debug=True)

form_result.html
<!doctype html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
        content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="../../static/css/style.css">
    <title>Form Submission Result</title>
</head>
<body>
    <header class="header">
        <div class="header__text">
            <h1>Form Submission Result</h1>
        </div>
    </header>
    <main>
        <div class="container">
            <h2>Form Data</h2>
            <ul>
                <li><strong>Name:</strong> {{ name }}</li>
                <li><strong>Email:</strong> {{ email }}</li>
                <li><strong>Address:</strong> {{ address }}</li>
                <li><strong>Date of Service:</strong> {{ date }}</li>
            </ul>
            <a href="/form">Return to Form</a>
        </div>
    </main>
    <footer>

    </footer>
</body>
</html>
