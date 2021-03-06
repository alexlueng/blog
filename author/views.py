from flask_blog import app
from flask import render_template, redirect, url_for, session, request
from author.form import RegisterForm, LoginForm
from author.models import Author
from author.decorators import login_required

@app.route('/login', methods=('GET', 'POST'))
def login():
	form = LoginForm()
	error = None

	if request.method == 'GET' and request.args.get('next'):
		session['next'] = request.args.get('next', None)
	if form.validate_on_submit():
		author = Author.query.filter_by(username=form.username.data, password=form.password.data).first()
		print(author)
		if author.count():
			session['username'] = form.username.data
			session['is_author'] = author.is_author
			if 'next' in session:
				next = session.get('next')
				session.pop('next')
				return redirect(next)
			else:
				return redirect(url_for('login_success'))
		else:
			error = "Incorrect username and password"
	return render_template('author/login.html', form=form, error=error)

@app.route('/register', methods=('GET', 'POST'))
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		return redirect(url_for('success'))
	return render_template('author/register.html', form=form)

@app.route('/success')
def success():
	return "Author registered success"

@login_required
@app.route('/login_success')
def login_success():
	return "Author login success"

@app.route('/logout')
def logout():
	session.pop('username')
	return redirect(url_for('index'))