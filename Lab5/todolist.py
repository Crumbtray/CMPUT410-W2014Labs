import sqlite3
from flask import Flask, request, redirect, url_for, g, render_template, flash, session, abort


DATABASE = 'test.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    return '<h1>Welcome to CMPUT 410 - Lab 5</h1>'

@app.route('/task', methods=['GET', 'POST'])
def task():
    if request.method == 'POST':
        if not session.get('logged_in'):
            abort(401)
        description = request.form['description']
        priority = request.form['priority']
        category = request.form['category']
        try:
            addTask(category, description, priority)
        except ValueError:
            flash('Error: Priority is not a number.')
            return redirect(url_for('task'))
        flash('New task was successfully posted')
        return redirect(url_for('task'))
    return render_template('show_entries.html', tasks=query_db('select * from tasks'))

@app.route('/delete', methods=['POST'])
def delete():
    if not session.get('logged_in'):
        abort(401)
    # !!! Your code here !!!
    taskId = request.form['id']
    removeTask(taskId)
    flash('Task was successfully deleted')
	# Hint: delete the task from database
    return redirect(url_for('task'))

@app.route('/edit/<taskId>', methods=['GET', 'POST'])
def edit(taskId):
    if request.method == 'POST':
        if not session.get('logged_in'):
            abort(401)
        newCategory = request.form['newCategory']
        newDescription = request.form['newDescription']
        newPriority = request.form['newPriority']
        try:
            updateTask(taskId, newCategory, newDescription, newPriority)
        except ValueError:
            flash('Error: Priority is not a number.')
            return redirect(url_for('edit', taskId=taskId))
        flash('Task was successfully edited.')
        return redirect(url_for('task'))

    return render_template('edit.html', task=query_db('select * from tasks where id=?', [taskId], one=True))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            # !!! Your code here !!!
            session['logged_in'] = True
			# Hint: set the session key
            return redirect(url_for('task'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('task'))

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def addTask(category, description, priority):
    query_db('insert into tasks (category, description, priority) values (?, ?, ?)',
             [category, description, int(priority)], one=True)
    get_db().commit()

def updateTask(taskId, newCategory, newDescription, newPriority):
    query_db('update tasks set category=?, description=?, priority=? where id=?', [newCategory, newDescription, int(newPriority), int(taskId)], one=True)
    get_db().commit();

def removeTask(taskId):
    query_db('delete from tasks where id=?',
             [int(taskId)], one=True)
    get_db().commit()

if __name__ == '__main__':
    app.debug = True
    app.run()
