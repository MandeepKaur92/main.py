from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>hello mandeep</h1>'

@app.route('/welcome')
def welcome():
    return render_template('hello.html')

@app.route('/welcome/<name>')
def welcome_name(name):
    return render_template('welcome.html', myname=name)
@app.route('/name')
def my_name():
    return 'Mandeep <h1>Kaur</h1>'
@app.route('/sum', methods=['GET'])
def add_number():
    a = request.args.get('a')
    b = request.args.get('b')
    c = int(a) + int(b)
    return 'sum : ' + str(c)
@app.route('/user-data', methods=['GET', 'POST'])
def user_data():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')

        result = '''  <h1>First Name : {}<h1>
                      <h1>Last Name : {}<h1> '''
        return result.format(first_name, last_name)
    return 'no get method allowed, only post method is accepted'

@app.route('/user')
def user_form():
    return '''
        <form method="POST" action="http://127.0.0.1:5000/user-data">
               <div><label>First Name: <input type="text" name="first_name"></label></div>
               <div><label>Last Name: <input type="text" name="last_name"></label></div>
               <input type="submit" value="Submit">
        </form>
    '''
if __name__ == '__main__':
    app.run()
