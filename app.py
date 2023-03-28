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


@app.route('/favorite-course', methods=['GET', 'POST'])
def favoritecourse():
    if request.method == 'POST':
        print('Course Subject: ' + request.form.get('course_subject'))
        print('Course Number: ' + request.form.get('course_number'))

    return render_template('favorite-course.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')

if __name__ == '__main__':
    app.run()
