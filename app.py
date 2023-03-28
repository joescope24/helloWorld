from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Joe Scopelliti! I am adding my first code change.'


@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/favorite-course')
def favoritecourse():  # put application's code here
    print('Course Subject: ' + request.args.get('course_subject'))
    print('Course Number: ' + request.args.get('course_number'))
    return render_template('favorite-course.html')

if __name__ == '__main__':
    app.run()
