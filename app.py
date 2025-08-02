from flask import Flask, render_template, request
from math import *

app = Flask(__name__, static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        operation = request.form['operation']
        number = float(request.form['number'])

        try:
            if operation == "sin" or "Sin":
                result = round(sin(radians(number)), 10)
            elif operation == "cos" or "Cos":
                result = round(cos(radians(number)), 10)
            elif operation == "tan" or "Tan":
                result = round(tan(radians(number)), 10)
            elif operation == "sec" or "Sec":
                result = round(1 / cos(radians(number)), 10)
            elif operation == "csc" or "Csc":
                result = round(1 / sin(radians(number)), 10)
            elif operation == "cot" or "Cot":
                result = round(1 / tan(radians(number)), 10)
            else:
                result = "Invalid Operation"
        except:
            result = "Math Error"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
