from flask import Flask, render_template, request
from password_strength import evaluate_password

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    pw = ''
    if request.method == 'POST':
        pw = request.form.get('password', '')
        result = evaluate_password(pw)
    return render_template('index.html', password=pw, result=result)

if __name__ == '__main__':
    app.run(debug=True)
