from module import SymptomCheck
from flask import Flask
from flask import *
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index2.html')


@app.route('/form', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        gender = request.form.get('gender')
        birth = int(request.form.get('birth'))
        number=request.form.get('number')

        return SymptomCheck(birth,number,gender)
    return render_template('form.html')
if __name__ == '__main__':
    app.run()
