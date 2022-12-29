from module import SymptomCheck
from flask import Flask
from flask import *
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = int(request.form.get('name'))
        username = int(request.form.get('username'))
        user=request.form.get("user")

        return SymptomCheck(name,username,user)
    return render_template('diagnose.html')
if __name__ == '__main__':
    app.run()