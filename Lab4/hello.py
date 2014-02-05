import sqlite3
from flask import Flask, request, redirect, url_for

app = Flask(__name__)
DATABASE = 'cmput410lab.db'
db = None

@app.route('/')
def welcome():
	return '<h1>Welcome to the CMPUT 410 - Lab 4</h1>'

@app.route("/task", methods=['GET', 'POST'])
def task():
	if request.method == 'POST':
		removeOption = request.form['remove']
		category = request.form['category']
		priority = int(request.form['priority'])
		description = request.form['desc']
		if removeOption == 'true':
			remove_task(category, priority, description)
		else:
			add_task(category, priority, description)
		return redirect(url_for('task'))

	# GET
	resp = ''
	# show input form
	resp = resp + '''
	<form action="" method=post>
		<p>Category <input type="text" name="category" /></p>
		<p>Priority <input type="text" name="priority" /></p>
		<p>Description <input type="text" name="desc" /></p>
		<input type=hidden name="remove" value="false" />
		<p><input type=submit value=Add></p>
	</form>'''

	# show table
	resp = resp + '''
	<table border="1" cellpadding="3">
		<tbody>
			<tr>
				<th>Category</th>
				<th>Priority</th>
				<th>Description</th>
				<th>Remove?</th>
			</tr>'''

	for task in query_db('select * from tasks'):
		resp = resp + '''<tr><td>%s</td><td>%s</td><td>%s</td><td>
		<form action="" method=post>
		<input type=hidden name= "category" value="%s" />
		<input type=hidden name="priority" value="%s" />
		<input type=hidden name="desc" value="%s" />
		<input type=hidden name="remove" value="true" />
		<input type=submit value="Remove" />
		</form></td></tr>''' % \
			(task['category'], task['priority'], task['description'], task['category'], task['priority'], task['description'])
	resp = resp + '''</tbody></table>'''
	return resp

def get_db():
	global db
	if db is None:
		db = sqlite3.connect(DATABASE)
		db.row_factory = sqlite3.Row
	return db

@app.teardown_appcontext
def close_connection(exception):
	global db
	if db is not None:
		db.close()
		db = None

def query_db(query, args=(), one=False):
	cur = get_db().cursor()
	print args
	cur.execute(query, args)
	rv = cur.fetchall()
	cur.close()
	return (rv[0] if rv else None) if one else rv

def add_task(category, priority, desc):
	query_db('insert into tasks (category, priority, description) values (?, ?, ?)', (category, priority, desc), one=True)
	get_db().commit()

def remove_task(category, priority, desc):
	query_db('delete from tasks where category=? and priority = ? and description = ?', (category, priority, desc), one=True)
	print "REMOVED"
	get_db().commit()


if __name__ == '__main__':
	app.debug = True
	app.run()