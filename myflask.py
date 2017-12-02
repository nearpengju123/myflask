# coding=utf-8

from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = '8\x0bm\xf3?\x8b\x919("\xab\xd4\x81,p.\xf3\xd7\xce?1\xefA\\'


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=10)


@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))


@app.route('/messages')
def messages():
    return render_template('messages.html')


@app.route('/tasks')
def tasks():
    return render_template('tasks.html')


@app.route('/ui')
def ui():
    return render_template('ui.html')


@app.route('/widgets')
def widgets():
    return render_template('widgets.html')


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/chart')
def chart():
    return render_template('chart.html')


@app.route('/typography')
def typography():
    return render_template('typography.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/table')
def table():
    return render_template('table.html')


@app.route('/calendar')
def calendar():
    return render_template('calendar.html')


@app.route('/filemanager')
def filemanager():
    return render_template('filemanager.html')


@app.route('/icon')
def icon():
    return render_template('icon.html')


@app.route('/login', methods=['get', 'post'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        print '%s:login in success' % session['username']
        return redirect(url_for('index'))
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    # app.run(host='192.168.1.103', port=5000)
    pass
