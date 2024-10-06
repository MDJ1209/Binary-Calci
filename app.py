# app.py - Flask app to handle the form submission

from flask import Flask, request, render_template

app = Flask(__name__)

def binary_to_decimal(binary):
    try:
        return str(int(binary, 2))
    except ValueError:
        return "Invalid binary number"

def decimal_to_binary(decimal):
    try:
        return bin(int(decimal))[2:]
    except ValueError:
        return "Invalid decimal number"

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        number = request.form['number']
        operation = request.form['operation']
        
        if operation == 'binary_to_decimal':
            result = binary_to_decimal(number)
        elif operation == 'decimal_to_binary':
            result = decimal_to_binary(number)
        else:
            result = "Invalid operation"

    return render_template('calci.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
